import numpy as np
import pandas as pd

filename = 'advertising.csv'
data = pd.read_csv(filename, index_col = 0)

# 建立3个自变量与目标变量的线性回归模型，计算误差。
X = data.iloc[:,0:3].values.astype(float)
y = data.iloc[:,3].values.astype(float)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()  
linreg.fit(X, y)

# 性能评估

#1. 将数据集分割为训练集和测试集
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)

#2. 在训练集上学习回归模型，在训练集和测试集上计算误差。
linregTr = LinearRegression() 
linregTr.fit(X_train, y_train)
print (linregTr.intercept_, linregTr.coef_)

#3.计算模型性能
from sklearn import metrics

predict_score =linregTr.score(X_test,y_test)
print('The decision coeficient is:{:.2f} '.format(predict_score) )
y_train_pred = linregTr.predict(X_train)
y_test_pred = linregTr.predict(X_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred) 
test_err = metrics.mean_squared_error(y_test, y_test_pred) 
print( 'The mean squar error of train and test are: {:.2f}, {:.2f}'.format(train_err, test_err) )

#4. 使用所有数据训练的模型性能测试
predict_score1 =linreg.score(X_test,y_test)
print('The decision coeficient of model trained with all is: {:.2f} '.format(predict_score1) )
y_test_pred1 = linreg.predict(X_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred1) 
print('The mean squar error of test with all: {:.2f}'.format(test_err1) )

#第二题
data1 = pd.read_csv(filename, index_col = 0, nrows=100)
#print(data1)
# 建立3个自变量与目标变量的线性回归模型，计算误差。
X = data1.iloc[:,0:3].values.astype(float)
y = data1.iloc[:,3].values.astype(float)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X, y)

# 性能评估

#1. 将数据集分割为训练集和测试集
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)

#2. 在训练集上学习回归模型，在训练集和测试集上计算误差。
linregTr = LinearRegression()
linregTr.fit(X_train, y_train)
print (linregTr.intercept_, linregTr.coef_)

#3.计算模型性能
from sklearn import metrics

predict_score =linregTr.score(X_test,y_test)
print('The decision coeficient is:{:.2f} '.format(predict_score) )
y_train_pred = linregTr.predict(X_train)
y_test_pred = linregTr.predict(X_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred)
test_err = metrics.mean_squared_error(y_test, y_test_pred)
print( 'The mean squar error of train and test are: {:.2f}, {:.2f}'.format(train_err, test_err) )

#4. 使用所有数据训练的模型性能测试
predict_score1 =linreg.score(X_test,y_test)
print('The decision coeficient of model trained with all is: {:.2f} '.format(predict_score1) )
y_test_pred1 = linreg.predict(X_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred1)
print('The mean squar error of test with all: {:.2f}'.format(test_err1) )