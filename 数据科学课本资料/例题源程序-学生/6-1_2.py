#例子6-1：将文本句子 “2018年世界杯小组赛抽签在莫斯科克里姆林宫举行”进行分词。

import jieba
print( jieba.lcut("2018年世界杯小组赛抽签在莫斯科克里姆林宫举行") )
print( jieba.lcut("2018年世界杯小组赛抽签在莫斯科克里姆林宫举行", cut_all = True) )
print( jieba.lcut_for_search("2018年世界杯小组赛抽签在莫斯科克里姆林宫举行") )

# 例6-2：显示例6-1分词后每个词的词性。
import jieba.posseg as pseg
words = pseg.cut("2018年世界杯小组赛抽签在莫斯科克里姆林宫举行")
for word, tag in words:
    print('word:{}, tag:{}'.format(word, tag) )
