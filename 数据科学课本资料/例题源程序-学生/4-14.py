import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon #导入Polygonx
from matplotlib.colors import rgb2hex  #导入rgb2hex
import pandas as pd
import numpy as np

#例3-14 绘制上海人口分布地图

#创建一个Figure对象
plt.figure(figsize=(16,8))     
#定义地图实例并绘制基本图
m = Basemap(llcrnrlon=120.8,llcrnrlat=30.5,urcrnrlon=122.2,urcrnrlat=31.9,projection='lcc',lat_1=30.4,lat_2=31.55,lon_0=121.5)  
#绘制上海各区边界
m.readshapefile('data/Shapefile/CHN_adm_shp/CHN_adm3', 'states', drawbounds=True)

#准备数据
data = pd.read_csv('data/ShanghaiGDP.csv',index_col='District')  #读取数据文件
statenames=[]    #区名列表初始化空
colors={}        #颜色字典初始化位空
cmap = plt.cm.YlOrRd  #设置颜色渐变方案
vmax = 800   #人口最大值
vmin =60     #人口最小值
print(data)

#对地图实例中的每个区根据区名称获取人口数量并转为颜色值
for shapedict in m.states_info:  
    statename = shapedict['NL_NAME_3']
    p = statename.split('|')  
    if len(p) > 1:
        s = p[1]
    else:
        s = p[0]
    s = s[:2]
    statenames.append(s)
    if s in data.index:
         pop = data['Population'][s]    #s区的人口数量
         colors[s] = cmap(np.sqrt((pop - vmin) / (vmax - vmin)))[:3] #s区颜色计算
    else:
         colors[s]=cmap(0,0,0)  #其他区颜色
#对每个区多边形填充颜色
    ax = plt.gca()    #获取当前子图
for nshape, seg in enumerate(m.states):
    color = rgb2hex(colors[statenames[nshape]])
    if color!=rgb2hex(cmap(0,0,0)):
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)
plt.show
        
  