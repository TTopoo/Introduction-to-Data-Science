#鸢尾花数据集聚类分析


#例5-5： 数据可视化分析，k-means聚类
#从数据集中读入数据
import pandas as pd
filename = 'data/iris.data'
data = pd.read_csv(filename, header = None)
data.columns = ['sepal length','sepal width','petal length','petal width','class']
data.iloc[0:5,:]

#绘制散点图矩阵，观察特征维度的区分度
import matplotlib.pyplot as plt
pd.plotting.scatter_matrix(data, diagonal='hist')
plt.show()

#生成k-means模型
X = data.iloc[:,0:4].values.astype(float)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

#输出聚类结果，使用‘petal length'和’petal width’绘制散点图，即X的2、3列
print('means.labels_:\n',kmeans.labels_)
pd.plotting.scatter_matrix(data, c=kmeans.labels_, diagonal='hist')
plt.show()

#比较数据类别标签与聚类结果 ARI（Adjusted Rand Index）
from sklearn import metrics
#将类名转换为整数值
data.loc[ data['class'] == 'Iris-setosa', 'class' ] = 0
data.loc[ data['class'] == 'Iris-versicolor', 'class' ] = 1
data.loc[ data['class'] == 'Iris-virginica', 'class' ] = 2
y = data['class'].values.astype(int)
print( 'ARI: ',metrics.adjusted_rand_score(y, kmeans.labels_) )

print( kmeans.labels_ )
sc = metrics.silhouette_score( X, kmeans.labels_, metric='euclidean' )
print('silhouette_score: ',sc)

#例5-6：“肘部”观察法，分析合理的簇值
clusters = [2,3,4,5,6,7,8]
sc_scores = []
#计算各个簇模型的轮廓系数
for i in clusters:
    kmeans = KMeans( n_clusters = i).fit(X)
    sc = metrics.silhouette_score( X, kmeans.labels_, metric='euclidean' )
    sc_scores.append( sc )

#绘制曲线图反应轮廓系数与簇数的关系
plt.plot(clusters, sc_scores, '*-')
plt.xlabel('Number of Clusters')
plt.ylabel('Sihouette Coefiicient Score')
plt.show()
