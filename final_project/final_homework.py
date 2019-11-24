# 读入数据
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import label_binarize
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn import preprocessing
from sklearn import tree
from sklearn.metrics import roc_curve, auc
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import final_homework_ui
from final_homework_ui import Ui_MainWindow
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')


class Performance:
    # 定义一个类，用来分类器的性能度量
    def __init__(self, labels, scores, threshold=0.5):
        # labels:数组类型，真实的标签 scores:数组类型，分类器的得分 param threshold:检测阈值
        self.labels = labels
        self.scores = scores
        self.threshold = threshold
        self.db = self.get_db()
        self.TP, self.FP, self.FN, self.TN = self.get_confusion_matrix()

    def accuracy(self):  # 正确率
        return (self.TP + self.TN) / (self.TP + self.FN + self.FP + self.TN)

    def presision(self):  # 准确率
        try:
            return self.TP / (self.TP + self.FP)
        except ZeroDivisionError as e:
            return -1
    def recall(self):  # 召回率
        try:
            return self.TP / (self.TP + self.FN)
        except ZeroDivisionError as e:
            return -1

    def _auc(self):  # auc值
        auc = 0.
        prev_x = 0
        xy_arr = self.roc_coord()
        for x, y in xy_arr:
            if x != prev_x:
                auc += (x - prev_x) * y
                prev_x = x
        return auc

    def roc_coord(self):  # roc坐标
        xy_arr = []
        tp, fp = 0., 0.
        neg = self.TN + self.FP
        pos = self.TP + self.FN
        for i in range(len(self.db)):
            tp += self.db[i][0]
            fp += 1 - self.db[i][0]
            try:
                xy_arr.append([fp / neg, tp / pos])
            except ZeroDivisionError as e:
                pass
        return xy_arr

    def roc_plot(self):  # 传参能手
        auc = self._auc()
        xy_arr = self.roc_coord()
        x = [_v[0] for _v in xy_arr]
        y = [_v[1] for _v in xy_arr]
        return x, y, auc

    def get_db(self):
        db = []
        for i in range(len(self.labels)):
            db.append([self.labels[i], self.scores[i]])
        db = sorted(db, key=lambda x: x[1], reverse=True)
        # print('db',db)#调试用
        return db

    def get_confusion_matrix(self):  # 计算混淆矩阵
        tp, fp, fn, tn = 0., 0., 0., 0.
        for i in range(len(self.labels)):
            if self.labels[i] == 1 and self.scores[i] >= self.threshold:
                tp += 1
            elif self.labels[i] == 0 and self.scores[i] >= self.threshold:
                fp += 1
            elif self.labels[i] == 1 and self.scores[i] < self.threshold:
                fn += 1
            else:
                tn += 1
        return [tp, fp, fn, tn]

# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)


class Mywindow(QtWidgets.QMainWindow, final_homework_ui.Ui_MainWindow):

    def __init__(self):
        super(Mywindow, self).__init__()
        # QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.F = MyFigure(width=2, height=1, dpi=100)
        # self.plotcos()
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)

        #############################################################################
        # 1-读取BilibiliUserInfo.csv文件数据
        pd.set_option('display.unicode.ambiguous_as_wide', True)
        pd.set_option('display.unicode.east_asian_width', True)
        c = ''
        self.data0 = pd.read_csv('BilibiliUserInfo.csv',index_col=0,low_memory=False)#没清洗的
        self.data1 = pd.read_csv('data2.csv',index_col=0,low_memory=False)#一轮清洗后
        self.data2 = []
        self.mlp = MLPClassifier()

        pd.set_option('max_colwidth', 20)  # 设置value的显示长度为100，默认为50

        '''
        self.dataMat, self.labelMat = self.loadDataSet('wine.data')
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.dataMat, self.labelMat,
                                                                                test_size=0.4, random_state=1)
        '''
        ###############################################################

        c = self.getInitAns()
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def getInitAns(self):
        c = '\n' + '读取BilibiliUserInfo.csv文件数据' + '\n' + str(self.data0) + '\n'
        c = c + '\n' + 'data2.csv文件数据' + '\n' + str(self.data1) + '\n'
        return c

    def p1_ck(self):  # 清洗数据前基本信息展示
        c = '清洗数据前基本信息展示 Running!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        labels0 = ['unknown','male', 'female', ]
        labels1 = ['common', 'vip1', 'vip2']
        sex = self.data0['sex'].value_counts()
        level = self.data0['level'].value_counts().sort_index()
        vip = self.data0['vipType'].value_counts()
        following = self.data0['following'].sort_index()
        try:
            level=level.drop('None')
        except KeyError as e:
            pass
        try:
            vip=vip.drop('None')
        except KeyError as e:
            pass

        self.F.fig.clf()
        self.F.axes = self.F.fig.add_subplot(221)
        self.F.axes1 = self.F.fig.add_subplot(222)
        self.F.axes2 = self.F.fig.add_subplot(212)

        self.F.axes.pie(sex,labels=labels0,explode=[0.1,0.1,0.1],autopct='%1.1f%%',startangle=0)
        self.F.axes.set_xlabel('Male to female ratio')
        self.F.axes1.pie(level,labels=level.index,explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,],autopct='%1.1f%%',startangle=0)
        self.F.axes1.set_xlabel('Rank distribution')
        self.F.axes2.pie(vip,labels=labels1,explode=[0.1,0.1,0.1],autopct='%1.1f%%',startangle=0)
        self.F.axes2.set_xlabel('Membership ratio')

        self.F.draw()

        c = '基本信息展示 Done!'
        print(self.data0.shape[0])
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def p2_ck(self):  # 清洗数据集，清洗数据后基本信息展示
        c = 'Data Cleansing!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        train = self.data1
        try:
            train.loc[train['sex'] == '保密', 'sex'] = 0
            train.loc[train['sex'] == '男', 'sex'] = 1
            train.loc[train['sex'] == '女', 'sex'] = 2
        except TypeError as e:
            pass

        print(train)
        try:
            z1 = train[train['face'].str.contains('noface')]
        except KeyError as e:
            z1 = train
        try:
            z1 = z1[z1['level'] == '0']
        except TypeError as e:
            pass
        try:
            z1 = z1[z1['bnum'] == 0]
        except TypeError as e:
            pass
        self.data1 = train.loc[train.index.difference(z1.index)]
        train = self.data1[['sex', 'level', 'following', 'fans', 'archiveview', 'bnum', 'vipType']]
        train.to_csv('biliTrain.csv', encoding='utf_8_sig')

        c = 'Done!    新生成数据集biliTrain.csv'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        self.data1 = train
        c = '清洗数据后基本信息展示 Running!'
        labels0 = ['unknown', 'male', 'female', ]
        sex = self.data1['sex'].value_counts()
        level = self.data1['level'].value_counts().sort_index()
        vip = self.data1['vipType'].value_counts()
        labels1 = ['common', 'vip1', 'vip2']

        self.F.fig.clf()
        self.F.axes = self.F.fig.add_subplot(221)
        self.F.axes1 = self.F.fig.add_subplot(222)
        self.F.axes2 = self.F.fig.add_subplot(212)

        self.F.axes.pie(sex, labels=labels0,explode=[0.1,0.1,0.1], autopct='%1.1f%%', startangle=0)
        self.F.axes.set_xlabel('Male to female ratio')
        self.F.axes1.pie(level, labels=level.index,explode=[0.3,0.3,0.3,0.1,0.1,0.1,0.1,], autopct='%1.1f%%', startangle=0)
        self.F.axes1.set_xlabel('Rank distribution')
        self.F.axes2.pie(vip, labels=labels1,explode=[0.1,0.1,0.1], autopct='%1.1f%%', startangle=0)
        self.F.axes2.set_xlabel('Membership ratio')

        self.F.draw()
        c = '\n\n基本信息展示 Done!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        X = self.data1.iloc[:, 0:6].values.astype(int)
        print(X[0:50])
        y = self.data1.iloc[:, 6].values.astype(int)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.1, random_state=1)
        #print(self.X_test.shape,self.y_test.shape)

    def p3_ck(self):  # SVM
        c = 'SVM Running!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        clf = svm.SVC()
        clf.fit(self.X_train[0:20000], self.y_train[0:20000])
        print(clf.score(self.X_test[0:5000], self.y_test[0:5000]))
        print("Classification report for %s" % clf)

        c = ("Performance on test set:", clf.score(self.X_test, self.y_test))
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        y_predicted = clf.predict(self.X_test)

        L = self.X_test.shape[0]
        xx = []
        yy = []
        aauc = []
        for k in range(3):  # 3类标签
            labels = []
            scores = []
            for i in range(L):
                if self.y_test[i] == k:
                    labels.append(1)
                else:
                    labels.append(0)
                if y_predicted[i] == k and y_predicted[i] == k:
                    scores.append(1)
                else:
                    scores.append(0)
                p = Performance(labels, scores)
            acc = p.accuracy()
            pre = p.presision()
            rec = p.recall()
            c = '类别' + str(k + 1) + ' accuracy: %.4f\n' % acc
            c = c + '类别' + str(k + 1) + ' precision: %.4f\n' % pre
            c = c + '类别' + str(k + 1) + ' recall: %.4f\n' % rec
            print(c)
            self.textBrowser.append(str(c))
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            x, y, auc = p.roc_plot()
            xx.append(x)
            yy.append(y)
            aauc.append(auc)
        colors = ['aqua', 'darkorange', 'cornflowerblue', ]
        AccScore = 0.0
        for i in range(L):  # 计算总的Acc
            if str(y_predicted[i]) == str(self.y_test[i]):
                AccScore += 1.0 / (L * 1.0)
        c = '正确率' + str(AccScore)

        self.F.fig.clf()
        self.F.axes3 = self.F.fig.add_subplot(111)
        for i, color in zip(range(3), colors):
            self.F.axes3.plot(xx[i], yy[i], color=color, lw=2, label='ROC curve of class {0} (area = {1:0.2f})'
                                                                    ''.format(i, aauc[i]))
        self.F.axes3.set_xlabel('False Positive Rate')
        self.F.axes3.set_ylabel('True Positive Rate')
        self.F.axes3.set_title('SVM ROC')
        self.F.axes3.legend(loc="lower right")
        self.F.draw()


        c = 'SVM Done!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def p4_ck(self):  # 决策树
        c = 'DTC Running!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        clf = tree.DecisionTreeClassifier()
        clf.fit(self.X_train, self.y_train)
        print("Classification report for %s" % clf)
        print("Performance on test set:", clf.score(self.X_test, self.y_test))
        predicted_y = clf.predict(self.X_test)
        print(predicted_y)
        L = self.X_test.shape[0]
        xx = []
        yy = []
        aauc = []
        for k in range(3):  # 3类标签
            labels = []
            scores = []
            for i in range(L):
                if self.y_test[i] == k:
                    labels.append(1)
                else:
                    labels.append(0)
                if predicted_y[i] <= k+0.5 and predicted_y[i] >= k-0.5:
                    scores.append(1)
                else:
                    scores.append(0)
                p = Performance(labels, scores)
            acc = p.accuracy()
            pre = p.presision()
            rec = p.recall()
            c = '类别' + str(k + 1) + ' accuracy: %.4f\n' % acc
            c = c + '类别' + str(k + 1) + ' precision: %.4f\n' % pre
            c = c + '类别' + str(k + 1) + ' recall: %.4f\n' % rec
            print(c)
            self.textBrowser.append(str(c))
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            x, y, auc = p.roc_plot()
            xx.append(x)
            yy.append(y)
            aauc.append(auc)
        colors = ['aqua', 'darkorange', 'cornflowerblue', ]
        AccScore = 0.0
        for i in range(L):  # 计算总的Acc
            if str(predicted_y[i]) == str(self.y_test[i]):
                AccScore += 1.0 / (L * 1.0)
        c = '正确率' + str(AccScore)

        self.F.fig.clf()
        self.F.axes3 = self.F.fig.add_subplot(111)
        for i, color in zip(range(3), colors):
            self.F.axes3.plot(xx[i], yy[i], color=color, lw=2, label='ROC curve of class {0} (area = {1:0.2f})'
                                                                    ''.format(i, aauc[i]))
        self.F.axes3.set_xlabel('False Positive Rate')
        self.F.axes3.set_ylabel('True Positive Rate')
        self.F.axes3.set_title('DTC ROC')
        self.F.axes3.legend(loc="lower right")
        self.F.draw()

        c = c + '\n\nDTC Done!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def p5_ck(self):  # MLP
        c = 'MLP Running!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        self.mlp.fit(self.X_train, self.y_train)
        c ="Train with complete data set: " + str(self.mlp.score(self.X_test, self.y_test))
        y_predicted = self.mlp.predict(self.X_test)
        print("Classification report for %s" % self.mlp)
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
        '''
        L = self.X_test.shape[0]
        xx = []
        yy = []
        aauc = []
        for k in range(3):  # 3类标签
            labels = []
            scores = []
            for i in range(L):
                if self.y_test[i] == k:
                    labels.append(1)
                else:
                    labels.append(0)
                if y_predicted[i] <= k + 0.5 and y_predicted[i] >= k - 0.5:
                    scores.append(1)
                else:
                    scores.append(0)
                p = Performance(labels, scores)
            acc = p.accuracy()
            pre = p.presision()
            rec = p.recall()
            c = '类别' + str(k + 1) + ' accuracy: %.4f\n' % acc
            c = c + '类别' + str(k + 1) + ' precision: %.4f\n' % pre
            c = c + '类别' + str(k + 1) + ' recall: %.4f\n' % rec
            print(c)
            self.textBrowser.append(str(c))
            self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
            x, y, auc = p.roc_plot()
            xx.append(x)
            yy.append(y)
            aauc.append(auc)
        colors = ['aqua', 'darkorange', 'cornflowerblue', ]
        AccScore = 0.0
        for i in range(L):  # 计算总的Acc
            if str(y_predicted[i]) == str(self.y_test[i]):
                AccScore += 1.0 / (L * 1.0)
        c = '正确率' + str(AccScore)
        
        self.F.fig.clf()
        self.F.axes3 = self.F.fig.add_subplot(111)
        for i, color in zip(range(3), colors):
            self.F.axes3.plot(xx[i], yy[i], color=color, lw=2, label='ROC curve of class {0} (area = {1:0.2f})'
                                                                     ''.format(i, aauc[i]))
        self.F.axes3.set_xlabel('False Positive Rate')
        self.F.axes3.set_ylabel('True Positive Rate')
        self.F.axes3.set_title('MLP ROC')
        self.F.axes3.legend(loc="lower right")
        self.F.draw()
        '''
        c = c + '\n\nMLP Done!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

    def p6_ck(self):  # K-Means
        c = 'K-Means Running!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        k = 2  # 聚类的类别
        iteration = 2  # 聚类最大循环次数
        data = self.data1
        data_zs = 1.0 * (data - data.mean()) / data.std()  # 数据标准化，std()表示求总体样本方差(除以n-1),numpy中std()是除以n
        print(data_zs)

        from sklearn.cluster import KMeans
        model = KMeans(n_clusters=k, max_iter=iteration)  # 分为k类
        # model = KMeans(n_clusters = k, n_jobs = 4, max_iter = iteration) #分为k类，并发数4
        model.fit(data_zs)  # 开始聚类

        # 简单打印结果
        r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
        r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
        r = pd.concat([r2, r1], axis=1)  # 横向连接（0是纵向），得到聚类中心对应的类别下的数目
        print('r',r)
        print('r.columns',r.columns)
        print(list(data.columns))
        r.columns = list(data.columns) +[u'Class Num']  # 重命名表头
        print(r)

        # 详细输出原始数据及其类别
        r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 详细输出每个样本对应的类别
        r.columns = list(data.columns) +[u'K-Means Num']  # 重命名表头

        from sklearn.manifold import TSNE
        tsne = TSNE()
        tsne.fit_transform(data_zs)  # 进行数据降维,并返回结果
        tsne = pd.DataFrame(tsne.embedding_, index=data_zs.index)  # 转换数据格式

        import matplotlib.pyplot as plt

        # 不同类别用不同颜色和样式绘图
        d = tsne[r[u'K-Means Num'] == 0]  # 找出聚类类别为0的数据对应的降维结果
        plt.plot(d[0], d[1], 'r.')
        d = tsne[r[u'K-Means Num'] == 1]
        plt.plot(d[0], d[1], 'go')
        #d = tsne[r[u'K-Means Num'] == 2]
        #plt.plot(d[0], d[1], 'b*')
        plt.show()

        c = c + '\n\nK-Means Done!'
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)
    def p7_ck(self):
        sex = int(self.spinBox.value())
        level = int(self.spinBox_1.value())
        following = int(self.spinBox_2.value())
        fans = int(self.spinBox_3.value())
        archiveview = int(self.spinBox_4.value())
        bnum = int(self.spinBox_5.value())
        X = np.array([[sex,level,following,fans,archiveview,bnum]])
        print(self.X_train[2])
        print(X)
        c = 'Predict:'
        ans = self.mlp.predict(X)
        c= c + str(ans)
        self.textBrowser.append(str(c))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)

        pass
# MAIN
app = QtWidgets.QApplication(sys.argv)
window = Mywindow()
window.show()
sys.exit(app.exec_())
