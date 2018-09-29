import tldextract
import  numpy as np
import time
import sklearn
from keras.models import load_model
from sklearn.cross_validation import train_test_split

def pad(dat, length=31, item=0):
    if len(dat)>length:
        dat=dat[:length]
    else:
        dat.extend((length-len(dat))*[item])
    return dat

def domain2list(domain):
    diction = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'0':27,'1':28,'2':29,'3':30,'4':31,'5':32,'6':33,'7':34,'8':35,'9':36,'-':37}
    data=[diction.get(x,38) for x in domain]
    return pad(data)

def makeData(black="./data/dga.txt"):
    X = []
    no_fetch_extract = tldextract.TLDExtract(suffix_list_urls=None)
    with open(black,'r') as f:
        data=f.readlines()
        for i in data:
            X.append(domain2list(no_fetch_extract(i.strip()).domain))
    X=np.mat(X)
    return X

# 获取模型
model = load_model("cnn-2121.h5")
# 输入测试集数据
data = makeData()
# 开始预测
# steps : 生成器返回数据的轮数,输出是恶意域名的概率
train_data, test_data = train_test_split(data,test_size=0.1)
starts=time.time()
model.predict(test_data,steps=1)
timecost=time.time()-starts
print(test_data.shape)
print(test_data.shape[0],"items")
print(timecost,"seconds")
print(test_data.shape[0]/timecost,"-eps")

