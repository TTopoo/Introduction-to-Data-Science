#例7-1 利用keras建立模型，训练鸢尾花数据集

from keras.models import Sequential
from keras.layers import Dense, Activation

# 定义模型结构
model = Sequential()
model.add(Dense(units=16, input_shape=(4,)))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(3))
model.add(Activation('softmax'))
#定义损失函数和优化器，并编译
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=["accuracy"])

import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import np_utils

filename = 'data\iris.data'
data = pd.read_csv(filename, header = None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']
data.iloc[0:5,:]

#数据预处理
#convert classname to integer
data.loc[ data['class'] == 'Iris-setosa', 'class' ] = 0
data.loc[ data['class'] == 'Iris-versicolor', 'class' ] = 1
data.loc[ data['class'] == 'Iris-virginica', 'class' ] = 2
#data
X = data.iloc[:,0:4].values.astype(float)
y = data.iloc[:,4].values.astype(int)
train_x, test_x, train_y, test_y = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

#keras多分类问题需要将类型转化为独热矩阵
#与pd.get_dummies()函数作用一致
train_y_ohe = np_utils.to_categorical(train_y, 3)
test_y_ohe = np_utils.to_categorical(test_y, 3)

#print(test_y_ohe )
#训练模型
model.fit(train_x, train_y_ohe, epochs=50, batch_size=1, verbose=2, validation_data=(test_x,test_y_ohe))

# 评估模型
loss, accuracy = model.evaluate(test_x, test_y_ohe, verbose=2)
print('loss = {},accuracy = {} '.format(loss,accuracy) )
# 查看预测结果
classes = model.predict(test_x, batch_size=1, verbose=2)
print('测试样本数：',len(classes))
print("分类概率:\n",classes)
