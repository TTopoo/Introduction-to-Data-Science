#实例 垃圾邮件识别

from sklearn.feature_extraction.text import CountVectorizer
import jieba
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
from sklearn import metrics

#构造文本分类特征集
train_file = open("data/mailcorpus.txt", 'r', encoding = "utf-8")
corpus = train_file.readlines()   #列表中的每个元素为一行文本
#分词
split_corpus = []
for c in corpus:
    split_corpus.append(" ".join(jieba.lcut(c)))
    
#使用词袋模型提取特征，得到文本特征矩阵
cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
X = cv.fit_transform(split_corpus).toarray()

#构造标签向量，垃圾标签为0，正常标签为1
y = [0] * 5000 + [1] * 5000

#将特征集 分为训练集和测试集
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.4, random_state = 0)

#使用SVM训练分类模型
svm = svm.SVC(kernel='rbf', gamma=0.7, C = 1.0)
svm.fit(X_train, y_train)

#SVM分类性能
y_pred_svm = svm.predict(X_test)

print("SVM accuracy:\n",svm.score(X_test, y_test))
print("SVM report:\n",metrics.classification_report(y_test, y_pred_svm))
print("SVM matrix:\n",metrics.confusion_matrix(y_test, y_pred_svm))

#使用朴素贝叶斯训练分类模型，给出分类效果
gnb = GaussianNB()
gnb.fit(X_train,y_train)

y_pred = gnb.predict(X_test)

#朴素贝叶斯模型分类效果
print("naive_bayes accuracy:\n",gnb.score(X_test, y_test))
print("naive_bayes report:\n",metrics.classification_report(y_test, y_pred))
print("naive_bayes matrix:\n",metrics.confusion_matrix(y_test, y_pred))
