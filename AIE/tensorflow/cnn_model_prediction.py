import tensorflow as tf
import os
from tensorflow.python.framework import graph_util
import  numpy as np
import time
import sklearn
from sklearn.cross_validation import train_test_split
from tensorflow.python.platform import gfile
import tldextract
'''
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
def makeData():
    X = []
    X.append(domain2list('oiooiakkkkk'))
    X=np.mat(X)
    return X

test = makeData()#测试数据

from tensorflow.python.platform import gfile

sess = tf.Session()
with gfile.FastGFile('D:/data/'+'model.pb', 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='') # 导入计算图

sess.run(tf.global_variables_initializer())#初始化

# 输入
input_x = sess.graph.get_tensor_by_name('input_x_:0')
op = sess.graph.get_tensor_by_name('output/main_output:0')

ret = sess.run(op,  feed_dict={input_x: test})
print (ret)
'''


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
    no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)
    with open(black,'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip()).domain))
    with open("./data/top-1m.csv",'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip().split(',')[1]).domain))
    X=np.mat(X)
    return X
data = makeData()
sess = tf.Session()
with gfile.FastGFile('D:/model/'+'model.pb', 'rb') as f:#打开模型文件
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='') # 导入计算图
sess.run(tf.global_variables_initializer())#初始化
# 输入
input_x = sess.graph.get_tensor_by_name('input_x_:0')
op = sess.graph.get_tensor_by_name('output/main_output:0')
train_data, test_data = train_test_split(data,test_size=0.1)
starts=time.time()
ret = sess.run(op,  feed_dict={input_x: test_data})
timecost=time.time()-starts
print(test_data.shape)
print(test_data.shape[0],"items")
print(timecost,"seconds")
print(test_data.shape[0]/timecost,"-eps")






'''
t = 5 #样本验证轮数
starts=time.time()
for i in range(t):
    starts_0=time.time()
    train_data, test_data = train_test_split(data,test_size=0.1)
    ret = sess.run(op,  feed_dict={input_x: test_data})
    timecost_0=time.time()-starts_0
    print(test_data.shape)
    print(test_data.shape[0],"items")
    print(timecost_0,"seconds")
    print(test_data.shape[0]/timecost_0,"-eps")

timecost=time.time()-starts_0
print('time:', timecost)
'''
