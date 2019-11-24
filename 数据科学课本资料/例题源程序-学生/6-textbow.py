from sklearn.feature_extraction.text import CountVectorizer
import jieba

#给出文档集，放在字符串列表中
corpus = [
    "我是中国人，我爱中国",
    "我是上海人",
    "我住在上海松江大学城"
    ]
split_corpus = [] #初始化存储jieba分词后的列表

#循环为corpus中的每个字符串分词
for c in corpus:
    #jieba分词后的字符串列表拼接为一个字符串，元素之间用空格分割
    s = " ".join(jieba.lcut(c)) #将分词得到的列表
    split_corpus.append(s) #将分词结果字符串添加到列表中
print(split_corpus)

#生成词袋
cv = CountVectorizer()
#修改token_pattern默认参数，保留单字符特征词
#cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")

cv_fit=cv.fit_transform(split_corpus)
print(cv.get_feature_names())  #显示特征列表
print(cv_fit.toarray())  #显示特征向量

#例6-4：使用例6.3中文档集，提取TF-IDF模型特征。
from sklearn.feature_extraction.text import TfidfTransformer  
tfidf_transformer = TfidfTransformer()
tfidf_fit = tfidf_transformer.fit_transform(cv_fit)

#显示TF-IDF特征向量
print(tfidf_fit.toarray())

