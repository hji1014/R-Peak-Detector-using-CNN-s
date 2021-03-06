import sys
import scipy.io
import numpy as np
from keras.utils import np_utils
import matplotlib.pyplot as plt
a=scipy.io.loadmat('104.mat')


ecg=a['signal']
ann=a['ann']
ecg=ecg[:,0]
ann=ann[:,0]
gl=[0]*650000
for i in ann:
	
	for j in range(i-40,i+40):
		gl[j]=1

x=[]
y=[]
for i in range(150,650000-150,200):
	x.append(ecg[i-150:i+150])
	y.append(gl[i])

x=np.array(x)
y=np.array(y)
#print(x.shape)
#plt.plot(y)
#plt.show()
x=x.reshape(3249,300,1)
y=np_utils.to_categorical(y)
y=y.reshape(3249,2)
#print(y[1:100])
from keras.models import Sequential
from keras.layers import LSTM,Conv1D,Dense,Activation,Flatten
model=Sequential()
#model.add(LSTM(2,activation='softmax',input_shape=(1,150)))
#model.add(Embedding(max_features,embedding_dims,input_length=maxlen))
model.add(Conv1D(1,30,activation='sigmoid',input_shape=(300,1)))
model.add(LSTM(50,input_shape=(1,271),return_sequences=True,activation='relu'))
model.add(Flatten())
model.add(Dense(2,activation='softmax'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
#model.fit(x,y,epochs=5,batch_size=35)
model.summary()
sys.exit(0)
a=scipy.io.loadmat('105.mat')
ecg=a['signal']
ann=a['ann']
ecg=ecg[:10000,0]
ann=ann[:,0]
gl=[0]*10000

x=[]
y=[]
for i in range(150,10000-150,1):
	x.append(ecg[i-150:i+150])
	y.append(gl[i])

x=np.array(x)
x.shape=(9700,300,1)
t=model.predict(x)
#print(type(t))
for l in range(len(t)):
	if(t[l][0]>0.5):
		t[l][0]=0
	else:
		t[l][0]=1
plt.plot(ecg[150:])
plt.plot(t[:,0])
plt.show()
