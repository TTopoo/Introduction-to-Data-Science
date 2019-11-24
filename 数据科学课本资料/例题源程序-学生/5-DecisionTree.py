#银行贷款偿还决策树分析

#读入数据
import pandas as pd

filename = 'data/bankdebt.csv'
data = pd.read_csv(filename, nrows = 5, index_col = 0, header = None)
print(data.values)
#data = pd.read_csv(filename, header = None)

#数据预处理
data = pd.read_csv(filename, index_col = 0, header = None)
data.loc[data[1] == 'Yes',1 ] = 1
data.loc[data[1] == 'No',1 ] = 0
data.loc[data[4] == 'Yes',4 ] = 1
data.loc[data[4] == 'No',4 ] = 0
data.loc[data[2] == 'Single',2 ] = 1
data.loc[data[2] == 'Married',2 ] = 2
data.loc[data[2] == 'Divorced',2] = 3
print( data.loc[1:5,:] )


#取data前4列数据作为特征属性值,最后一列作为分类值
X = data.loc[ :, 1:3 ].values.astype(float)
y = data.loc[ :, 4].values.astype(int)

#训练模型，预测样本分类
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
clf.score(X,y)

#评估分类器性能,计算混淆矩阵，Precision 和 Recall
predicted_y = clf.predict(X)
from sklearn import metrics
print(metrics.classification_report(y, predicted_y))
print('Confusion matrix:' )
print( metrics.confusion_matrix(y, predicted_y) )

#生成并显示决策树图
featureName =['House', 'Marital', 'Income']
className = ['Cheat','Not Cheat']
#生成图
from graphviz import Source
graph = Source( tree.export_graphviz(clf, out_file=None, feature_names=featureName,class_names=className))
#保存到文件中并显示
png_bytes = graph.pipe(format='png')
with open('dectree.png','wb') as f:
    f.write(png_bytes)
from IPython.display import Image
Image(png_bytes)
