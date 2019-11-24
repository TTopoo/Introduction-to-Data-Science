#例5-7  前馈神经网络 鸢尾花数据集分类

#从数据集中读入数据
import pandas as pd
filename = 'data\iris.data'
data = pd.read_csv(filename, header = None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']
data.iloc[0:5,:]

#计算数据集中每种类别样本数，并给出统计特征
print( data['class'].value_counts() )
data.groupby('class').mean()
data.groupby('class').var()

#数据预处理
#convert classname to integer
data.loc[ data['class'] == 'Iris-setosa', 'class' ] = 0
data.loc[ data['class'] == 'Iris-versicolor', 'class' ] = 1
data.loc[ data['class'] == 'Iris-virginica', 'class' ] = 2

import matplotlib.pyplot as plt
pd.plotting.scatter_matrix(data, c=data['class'].values, diagonal='hist')
plt.show()

#data
X = data.iloc[:,0:4].values.astype(float)
y = data.iloc[:,4].values.astype(int)

#训练神经网络分类器模型
from sklearn.neural_network import MLPClassifier
#创建一个2层隐层，每层5个结点
mlp = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5, 5), random_state=1)
mlp.fit(X,y)
print("Train with complete data set: ",mlp.score(X,y))

from sklearn import metrics
y_predicted = mlp.predict(X)
print("Classification report for %s" % mlp)

print(metrics.classification_report(y, y_predicted) )
print( "Confusion matrix:\n", metrics.confusion_matrix(y, y_predicted) )

