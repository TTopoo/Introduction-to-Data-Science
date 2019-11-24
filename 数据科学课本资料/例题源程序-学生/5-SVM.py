#例5-4 银行投资业务推广SVM分析

#读入数据
import pandas as pd

filename = 'data/bankpep.csv'
data = pd.read_csv(filename, index_col = 'id')
print( data.iloc[0:5,:])

#将最数据中的‘YES’和‘NO'转换成代表分类的整数 1 和 0
seq = ['married', 'car', 'save_act', 'current_act', 'mortgage', 'pep']
for feature in seq :  # 逐个特征进行替换
    data.loc[ data[feature] == 'YES', feature ] =1
    data.loc[ data[feature] == 'NO', feature ] =0

#将性别转换为整数1和0
data.loc[ data['sex'] == 'FEMALE', 'sex'] =1
data.loc[ data['sex'] == 'MALE', 'sex'] =0
print(data[0:5])

#将离散特征数据进行独热编码，转换为dummies矩阵
dumm_reg = pd.get_dummies( data['region'], prefix='region' )
#print(dumm_reg[0:5])

dumm_child = pd.get_dummies( data['children'], prefix='children' )
#print(dumm_child[0:5])

#删除dataframe中原来的两列后再 jion dummies
df1 = data.drop(['region','children'], axis = 1)
#print( df1[0:5])
df2 = df1.join([dumm_reg,dumm_child], how='outer')
print( df2[0:2])

#准备训练输入变量
X = df2.drop(['pep'], axis=1).values.astype(float)
#X = df2.iloc[:,:-1].values.astype(float)
y = df2['pep'].values.astype(int)
print("X.shape", X.shape)
print(X[0:2,:])
print(y[0:2])

#训练模型，评价分类器性能
from sklearn import svm
from sklearn import metrics
clf = svm.SVC(kernel='rbf', gamma=0.6, C = 1.0)
clf.fit(X, y)
print( "Accuracy：",clf.score(X, y) )
y_predicted = clf.predict(X)
print( metrics.classification_report(y, y_predicted) )

#将数据集拆分为训练集和测试集，在测试集上查看分类效果
from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=1)
clf = svm.SVC(kernel='rbf', gamma=0.7, C = 1.0)
clf.fit(X_train, y_train)
print("Performance on training set:", clf.score(X_train, y_train) )
print("Performance on test set:", clf.score(X_test, y_test) )

#对不同方差的数据标准化
from sklearn import preprocessing
X_scale = preprocessing.scale(X)

#将标准化后的数据集拆分为训练集和测试集，在测试集上查看分类效果
X_train, X_test, y_train, y_test = model_selection.train_test_split(X_scale, y, test_size=0.3, random_state=1)
clf = svm.SVC(kernel='poly', gamma=0.6, C = 0.001)
clf.fit(X_train, y_train)
print( clf.score(X_test, y_test) )

#查看在测试集上混淆矩阵，Precision、Recall和F1
y_predicted = clf.predict(X_test)
print("Classification report for %s" % clf)

print (metrics.classification_report(y_test, y_predicted) )
print( "Confusion matrix:\n", metrics.confusion_matrix(y_test, y_predicted) )





