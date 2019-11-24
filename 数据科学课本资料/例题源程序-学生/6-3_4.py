#例6-3：提取文档集的词袋特征

from sklearn.feature_extraction.text import CountVectorizer
import jieba
#给出文档集，放在字符串列表中
corpus = ["我是中国人，我爱中国", "我是上海人", "我住在上海松江大学城" ]
split_corpus = [] #初始化存储jieba分词后的列表
#循环为corpus中的每个字符串分词
for c in corpus:
    #将jieba分词后的字符串列表拼接为一个字符串，元素之间用" "分割
    s = " ".join(jieba.lcut(c)) #将分词得到的列表
    split_corpus.append(s) #将分词结果字符串添加到列表中
print(split_corpus)
#生成词袋
cv = CountVectorizer()
cv_fit=cv.fit_transform(split_corpus)
print(cv.get_feature_names())  #显示特征列表
print(cv_fit.toarray())  #显示特征向量

#修改token_pattern默认参数,保留所有词特征
cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
cv_fit=cv.fit_transform(split_corpus)
print(cv.get_feature_names())  #显示特征列表
print(cv_fit.toarray())  #显示特征向量


#例6-4：提取TF-IDF模型特征。

#第一种方法：将词袋特征转化为TF-IDF特征
from sklearn.feature_extraction.text import TfidfTransformer  
tfidf_transformer = TfidfTransformer()
tfidf_fit = tfidf_transformer.fit_transform(cv_fit)
#显示TF-IDF特征向量
print(tfidf_fit.toarray())

#第二种方法：直接使用feature_extraction.text模块的TfidfVectorizer类
from sklearn.feature_extraction.text import TfidfVectorizer
#直接用分词后得到的列表计算TF-IDF特征表示
tfidf = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
tfidf_fit=tfidf.fit_transform(split_corpus)
print(tfidf_fit.toarray()) #显示TF-IDF特征向量
