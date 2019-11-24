#例5-1 广告收益预测分析，回归分析方法

#1.从文件中读入数据，忽略第0行
import numpy as np
import pandas as pd

filename = 'data/advertising.csv'
data = pd.read_csv(filename, index_col = 0)

#print(data.iloc[0:5, :].values)
print(data[0:5])


#导入绘图库
import matplotlib.pyplot as plt
#2.绘制自变量与目标变量之间的散点图,电视广告与销量之间的关联
data.plot(kind='scatter',x='TV',y='Sales',title='Sales with Advertising on TV')
plt.xlabel("TV")
plt.ylabel("sales")
plt.show()

#微博广告与销量之间的关联
data.plot(kind='scatter',x='Weibo',y='Sales',title='Sales with Advertising on Weibo')
plt.xlabel("Weibo")
plt.ylabel("sales")
plt.show()

#微信广告与销量之间的关联
data.plot(kind='scatter',x='WeChat',y='Sales',title='Sales with Advertising on WeChat')
plt.xlabel("WeChat")
plt.ylabel("sales")
plt.show()

#3. 建立3个自变量与目标变量的线性回归模型，计算误差。
X = data.iloc[:,0:3].values.astype(float)
y = data.iloc[:,3].values.astype(float)
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()  
linreg.fit(X, y)
#输出线性回归模型的截距和回归系数
print (linreg.intercept_, linreg.coef_)

#4.保存回归模型导文件，以便后续加载使用
from sklearn.externals import joblib
joblib.dump(linreg, 'linreg.pkl')   #保存至文件

#重新加载预测数据
import numpy as np
load_linreg = joblib.load('linreg.pkl')  #从文件读取模型
new_X = np.array([[130.1,87.8,69.2]])
print("6月广告投入：",new_X)
print("预期销售：",load_linreg.predict(new_X) ) #使用模型预测


#例5-2 性能评估

#1. 将数据集分割为训练集和测试集
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.35, random_state=1)

#2. 在训练集上学习回归模型，在训练集和测试集上计算误差。
linregTr = LinearRegression() 
linregTr.fit(X_train, y_train)
print (linregTr.intercept_, linregTr.coef_)

#3.计算模型性能
from sklearn import metrics
y_train_pred = linregTr.predict(X_train)
y_test_pred = linregTr.predict(X_test)
train_err = metrics.mean_squared_error(y_train, y_train_pred) 
test_err = metrics.mean_squared_error(y_test, y_test_pred) 
print( 'The mean squar error of train and test are: {:.2f}, {:.2f}'.format(train_err, test_err) )

predict_score =linregTr.score(X_test,y_test)
print('The decision coeficient is:{:.2f} '.format(predict_score) )

#4. 使用所有数据训练的模型性能测试
predict_score1 =linreg.score(X_test,y_test)
print('The decision coeficient of model trained with all is: {:.2f} '.format(predict_score1) )
y_test_pred1 = linreg.predict(X_test)
test_err1 = metrics.mean_squared_error(y_test, y_test_pred1) 
print( 'The mean squar error of test with all: {:.2f}'.format(test_err1) )
