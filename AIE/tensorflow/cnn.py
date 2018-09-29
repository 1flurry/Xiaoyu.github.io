import os
import sys
import time
from datetime import timedelta
import numpy as np
import tensorflow as tf
import sklearn
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import tldextract
from tensorflow.python.framework import graph_io
from tensorflow.python.framework import graph_util

'''数据预处理'''
def pad(dat, length=31, item=0):
    if len(dat)>length:
        dat=dat[0:length]
    else:
        dat.extend((length-len(dat))*[item])
    return dat
def domain2list(domain):
    diction = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'0':27,'1':28,'2':29,'3':30,'4':31,'5':32,'6':33,'7':34,'8':35,'9':36,'-':37}
    data=[diction.get(x,38) for x in domain]
    return pad(data)
def makeData(black="./data/dga.txt",white="./data/top-1m.csv"):
    X = []
    Y = []
    no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)
    with open(black,'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip()).domain))
            Y.append([0])
    with open("./data/top-1m.csv",'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip().split(',')[1]).domain))
            Y.append([1])
    X=np.mat(X)
    Y=np.mat(Y)
    return X,Y
def batch_iter(x, y, batch_size=512):
    """生成批次数据"""
    data_len = len(x)
    num_batch = int((data_len - 1) / batch_size) + 1

    indices = np.random.permutation(np.arange(data_len))
    x_shuffle = x[indices]
    y_shuffle = y[indices]

    for i in range(num_batch):
        start_id = i * batch_size
        end_id = min((i + 1) * batch_size, data_len)
        yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]

'''获取已使用时间'''
def get_time_dif(start_time):
    end_time = time.time()
    time_dif = end_time - start_time
    return timedelta(seconds=int(round(time_dif)))

'''评估在某一数据上的准确率和损失'''
def evaluate(sess, x_, y_,loss,acc):

    data_len = len(x_)
    batch_eval = batch_iter(x_, y_, batch_size)
    total_loss = 0.0
    total_acc = 0.0
    loss = tf.reduce_mean(cross_entropy)

    for x_batch, y_batch in batch_eval:
        batch_len = len(x_batch)
        loss_n, acc_n = sess.run([loss, acc], feed_dict={input_x: x_batch,input_y: y_batch,keep_prob: 0.25})
        total_loss += loss_n * batch_len
        total_acc += acc_n * batch_len
    return total_loss / data_len, total_acc / data_len

if __name__ == '__main__':
    '''模型参数'''
    embedding_dim = 4                     # 词向量维度
    seq_length = 31                       # 序列长度
    num_classes = 1                       # 类别数
    num_filters = 20                      # 卷积维度
    kernel_size = 3                       # 卷积核尺寸
    vocab_size = 39                       # 词汇表达小
    dropout_keep_prob = 0.75              # dropout保留比例
    learning_rate = 0.001                 # 学习率
    batch_size = 1024                     # 每批训练大小
    num_epochs = 20                       # 总迭代轮次
    print_per_batch = 1000                # 每多少轮输出一次结果
    save_per_batch = 1000                 # 每多少轮存入tensorboard
    output_graph_name = 'model.pb'        # 保存模型文件名
    output_fld = '/model/'                # 保存路径
    '''载入训练集与验证集'''
    print("Loading training and validation data...")
    X,Y=makeData()
    #vocab_size = len(X)
    x_train, x_val, y_train, y_val = train_test_split(X,Y,test_size=0.1)
    print(x_train.shape)
    print(y_train.shape)
    print(x_val.shape)
    print(y_val.shape)
    del X,Y

    '''建立模型'''
    print('Configuring CNN model...')
    # 待输入的数据
    #with tf.Graph().as_default() as g:
    input_x = tf.placeholder(tf.int32, [None, seq_length], name='input_x_')
    input_y = tf.placeholder(tf.float32, [None, num_classes], name='input_y_')
    keep_prob = tf.placeholder(tf.float32, name='dropout_keep_prob')
    #创建cnn模型
    with tf.device('/cpu:0'):#强制在CPU上执行操作
        embedding = tf.get_variable('embedding', [vocab_size, embedding_dim])
        embedding_inputs = tf.nn.embedding_lookup(embedding, input_x)
    with tf.name_scope("cnn"):
        conv_1 = tf.layers.conv1d(embedding_inputs, num_filters, kernel_size, name='conv_1')
        maxp = tf.layers.max_pooling1d(conv_1, 2, 2)
        conv_2 = tf.layers.conv1d(maxp, num_filters, kernel_size, name='conv_2')
        maxp = tf.layers.max_pooling1d(conv_2, 2, 2)
        flatten = tf.contrib.layers.flatten(maxp)
    with tf.name_scope("score"):
        # 全连接层，后面接dropout以及sigmoid激活
        fc = tf.layers.dropout(flatten,0.25)
        fc = tf.layers.dense(fc, 16, name='fc1')
        fc = tf.layers.dense(fc, num_classes, name='fc2')
    with tf.name_scope('output'):
    	#输出层
        logits = tf.nn.sigmoid(fc, name='main_output')
    with tf.name_scope("optimize"):
        # 损失函数，交叉熵
        cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=input_y)
        loss = tf.reduce_mean(cross_entropy)
        # 优化器
        optim = tf.train.RMSPropOptimizer(learning_rate=learning_rate).minimize(loss)
    with tf.name_scope("accuracy"):
        # 准确率
        logits = tf.cast(logits, tf.int32)
        y = tf.cast(input_y, tf.int32)
        correct_pred = tf.equal(logits, y)
        acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
    tf.summary.scalar("loss", loss)
    tf.summary.scalar("accuracy", acc)
    merged_summary = tf.summary.merge_all()

    '''创建session'''
    session = tf.Session()
    session.run(tf.global_variables_initializer())
    
    '''训练模型'''
    print('Training and evaluating...')
    start_time = time.time()
    total_batch = 0  # 总批次
    best_acc_val = 0.0  # 最佳验证集准确率
    last_improved = 0  # 记录上一次提升批次
    require_improvement = 40000  # 如果超过40000轮未提升，提前结束训练
    flag = False
    for epoch in range(num_epochs):
        print('Epoch:', epoch + 1)
        batch_train = batch_iter(x_train, y_train, batch_size)
        for x_batch, y_batch in batch_train:
            #feed_dict = feed_data(x_batch, y_batch, 0.75)
            feed_dict = {input_x: x_batch,input_y: y_batch,keep_prob: dropout_keep_prob}
            if total_batch % print_per_batch == 0:
                # 每多少轮次输出在训练集和验证集上的性能
                loss_train, acc_train = session.run([loss, acc], feed_dict={input_x: x_batch,input_y: y_batch,keep_prob: dropout_keep_prob})
                loss_val, acc_val = evaluate(session, x_val, y_val, loss, acc)  # todo
                time_dif = get_time_dif(start_time)
                msg = 'Iter: {0:>6}, Train Loss: {1:}, Train Acc: {2:>7.2%},' \
                    + ' Val Loss: {3:>6.2}, Val Acc: {4:>7.2%}, Time: {5}'
                print(msg.format(total_batch, loss_train, acc_train, loss_val, acc_val, time_dif))
    
            session.run(optim, feed_dict=feed_dict)  # 运行优化
            total_batch += 1
            if total_batch - last_improved > require_improvement:
                # 验证集正确率长期不提升，提前结束训练
                print("No optimization for a long time, auto-stopping...")
                flag = True
                break  # 跳出循环
        #session.run(tf.assign(learning_rate, 0.001 * (0.95 ** epoch)),float32)#逐步降低学习率
        #learning_rate = session.run(lr)
        if flag:  # 同上
            break

    '''保存模型'''
    if not os.path.exists(output_fld):
        os.makedirs(output_fld)
    with tf.Graph().as_default() as g:
        graph = session.graph
        input_graph_def = graph.as_graph_def()
        graph_util.convert_variables_to_constants
        constant_graph = graph_util.convert_variables_to_constants(session, input_graph_def, output_node_names=['output/main_output'])
        #由于采用了name_scope所以在main_output之前需要加上score/
    with tf.gfile.FastGFile(output_fld+output_graph_name, mode='wb') as f:
        f.write(constant_graph.SerializeToString())

        
