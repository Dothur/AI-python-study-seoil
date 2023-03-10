from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
mnist=fetch_openml('mnist_784')
mnist.data=mnist.data/255.0
x_train=mnist.data[:60000]; x_test=mnist.data[60000:]
y_train=np.int16(mnist.target[:60000]); y_test=np.int16(mnist.target[60000:])

# MLP 분류기 모델을 학습
mlp1=MLPClassifier(hidden_layer_sizes=(100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=True)
mlp2=MLPClassifier(hidden_layer_sizes=(100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=True)
mlp3=MLPClassifier(hidden_layer_sizes=(100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=True)
mlp4=MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=True)
mlp5=MLPClassifier(hidden_layer_sizes=(100, 100, 100, 100, 100),learning_rate_init=0.001,batch_size=512,max_iter=300,solver='adam',verbose=True)

mlp1.fit(x_train,y_train)
mlp2.fit(x_train,y_train)
mlp3.fit(x_train,y_train)
mlp4.fit(x_train,y_train)
mlp5.fit(x_train,y_train)

# 테스트 집합으로 예측
res1=mlp1.predict(x_test)
res2=mlp2.predict(x_test)
res3=mlp3.predict(x_test)
res4=mlp4.predict(x_test)
res5=mlp5.predict(x_test)

# 혼동 행렬
conf1=np.zeros((10,10),dtype=np.int16)
conf2=np.zeros((10,10),dtype=np.int16)
conf3=np.zeros((10,10),dtype=np.int16)
conf4=np.zeros((10,10),dtype=np.int16)
conf5=np.zeros((10,10),dtype=np.int16)

for i in range(len(res1)):
    conf1[res1[i]][y_test[i]]+=1
    conf2[res2[i]][y_test[i]]+=1
    conf3[res3[i]][y_test[i]]+=1
    conf4[res4[i]][y_test[i]]+=1
    conf5[res5[i]][y_test[i]]+=1

print(conf1)
print(conf2)
print(conf3)
print(conf4)
print(conf5)

# 정확률 계산
no_correct1=0
no_correct2=0
no_correct3=0
no_correct4=0
no_correct5=0

for i in range(10):
    no_correct1+=conf1[i][i]
    no_correct2+=conf2[i][i]
    no_correct3+=conf3[i][i]
    no_correct4+=conf4[i][i]
    no_correct5+=conf5[i][i]

accuracy1=no_correct1/len(res1)
accuracy2=no_correct2/len(res2)
accuracy3=no_correct3/len(res3)
accuracy4=no_correct4/len(res4)
accuracy5=no_correct5/len(res5)

print("(은닉층 1개) 테스트 집합에 대한 정확률은", accuracy1*100, "%입니다.")
print("(은닉층 2개) 테스트 집합에 대한 정확률은", accuracy2*100, "%입니다.")
print("(은닉층 3개) 테스트 집합에 대한 정확률은", accuracy3*100, "%입니다.")
print("(은닉층 4개) 테스트 집합에 대한 정확률은", accuracy4*100, "%입니다.")
print("(은닉층 5개) 테스트 집합에 대한 정확률은", accuracy5*100, "%입니다.")
