import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import numpy as np

#例4-13：绘制上海GDP地图

#创建一个Figure对象
plt.figure(figsize=(16,8))     
#定义地图实例并绘制基本图
#m = Basemap(llcrnrlon=77,llcrnrlat=14,urcrnrlon=140,urcrnrlat=51,projection='lcc',lat_1=33,lat_2=45,lon_0=100)

m = Basemap(llcrnrlon=120.8,llcrnrlat=30.5,urcrnrlon=122.2,urcrnrlat=31.9,projection='lcc',lat_1=30.4,lat_2=31.55,lon_0=121.5)
#m.drawstates(linewidth=3)     #绘制省边界
    
#绘制上海各区边界
m.readshapefile('data/Shapefile/CHN_adm_shp/CHN_adm3', 'County', drawbounds=True)

#准备数据，绘制GDP数据点
data = pd.read_csv('data/ShanghaiGDPPinyin.csv',index_col='District')  #读取数据文件
print(data)

lat = np.array(data["Latitude"])    # 获取各区纬度值
lon = np.array(data["Longitude"])   # 获取各区经度值
gdp = np.array(data["GDP"])         # 获取GDP值

size=(gdp/np.max(gdp))*1000       # 绘制散点图时GDP值对应点的大小
x,y = m(lon,lat)                  # 确定各区经纬度坐标点
m.scatter(x,y,s=size)             #在地图上绘制散点图

# 绘制经线和纬线
parallels = np.arange(30.5,31.9,0.5) 
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10) # 绘制纬线

meridians = np.arange(120.5,122.2,0.5)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10) # 绘制经线

#m.etopo() # 绘制地形图，浮雕样式

