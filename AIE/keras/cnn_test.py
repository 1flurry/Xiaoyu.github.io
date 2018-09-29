# coding: utf-8

import numpy as np
import tldextract
import keras

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM,GRU

from keras.layers import  Bidirectional

import sklearn
from sklearn.cross_validation import train_test_split
import sys   
def pad(dat, length=31, item=0):
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
            Y.append(1)
    with open("./data/top-1m.csv",'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip().split(',')[1]).domain))
            Y.append(0)

    X=np.mat(X)
    Y=np.mat(Y)
    return X,Y.T

'''
def build_model(max_features, maxlen):
    #双向""Build bi-GRU model""
    # 定义顺序模型
    model = Sequential()
    model.add(Embedding(max_features, 
                        32, #输出维度
                        input_length=maxlen))
    model.add(Bidirectional(GRU(16)))
    model.add(Dropout(0.25)) #断开神经元的概率，防止过拟合
    model.add(Dense(16,activation="relu")) #int 输出维度
    model.add(Dense(1)) #int 输出维度
    model.add(Activation('sigmoid'))
    keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)                        
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    
    return model

'''
from keras.layers import Conv1D, MaxPooling1D,Flatten
def build_model(max_features, maxlen):
    """Build cnn model"""
    model = Sequential()
    model.add(Embedding(max_features, 
                        8, #输出维度
                        input_length=maxlen))
    model.add(Conv1D(16,3))
    model.add(MaxPooling1D(2))
    model.add(Conv1D(16,3))
    model.add(MaxPooling1D(2))
    model.add(Flatten())
    model.add(Dropout(0.25))
    model.add(Dense(16))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                 metrics=['accuracy'])

    return model


import time

timestamp=time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
print('Get data...')
X,Y=makeData()
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                Y, 
                                                test_size=0.1)
del X,Y
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)


print('Build model...')

max_features=39
maxlen=31
model = build_model(max_features, maxlen)
#plot_model(model, to_file='model.png',show_shapes=True)
model.summary()


batch_size=512
print('Training start...')
model.fit(X_train, y_train, #训练集
          validation_data=(X_test, y_test), #验证集
          batch_size=batch_size,
          verbose=1, # 进度条显示
          epochs=5) # 迭代次数
print('Training Done!')



fileprefix="bigru"
model.save(fileprefix+".krs")


# In[8]:


test_dat = X_test[:]
print(test_dat.shape)
starts=time.time()
results=model.predict_classes(test_dat,batch_size=512)
timecost=time.time()-starts
print(test_dat.shape[0],"items")
print(timecost,"seconds")
print(test_dat.shape[0]/timecost,"-eps")

