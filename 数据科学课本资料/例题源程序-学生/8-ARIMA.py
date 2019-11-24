#例8-2 ARIMA建模分析

#1）绘制时序图
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/stockClose.csv', index_col = '日期',encoding='ANSI')
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
data.plot()
plt.show()

#2）纯随机性和平稳性检验
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(data)                           #自相关图
plt.show()
from statsmodels.stats.diagnostic import acorr_ljungbox
print('白噪声-检验结果：', acorr_ljungbox(data['股价'], lags=1))
from statsmodels.tsa.stattools import adfuller as ADF
print('ADF-检验结果：', ADF(data['股价']))

#3）差分转换
from statsmodels.graphics.tsaplots import plot_pacf
D_data = data.diff().dropna() #对原数据进行1阶差分，删除非法值
D_data.columns = ['股价差分']
D_data.plot()  #时序图
plot_acf(D_data) #自相关图
plot_pacf(D_data) #偏自相关图
plt.show()
print('差分序列－ADF－检验结果为：', ADF(D_data[u'股价差分'])) #平稳性检测

#4)定阶
from statsmodels.tsa.arima_model import ARIMA
data['股价'] = data['股价'].astype(float)
pmax = int(len(D_data)/10) #一般阶数不超过length/10
qmax = int(len(D_data)/10) #一般阶数不超过length/10
e_matrix = [] #评价矩阵
for p in range(pmax+1):
    tmp = []
    for q in range(qmax+1):
        try: #存在部分报错，所以用try来跳过报错。
            tmp.append(ARIMA(data, (p,1,q)).fit().aic)
        except:
            tmp.append(None)
    e_matrix.append(tmp)
e_matrix = pd.DataFrame(e_matrix) #从中可以找出最小值
p,q = e_matrix.stack().idxmin() #先用stack展平，然后用找出最小值位置。
print('AIC最小的p值和q值为：%s、%s' %(p,q))

#5）预测
model = ARIMA(data, (p,1,q)).fit() #建立ARIMA(4,1,1)模型
model.summary2()  　#给出模型报告
model.forecast(5)   #作为期5天的预测，返回预测结果、标准误差、置信区间。
