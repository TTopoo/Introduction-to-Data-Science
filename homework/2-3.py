import numpy as np
import pandas as pd

datadata=pd.read_csv('datingTestSet.csv',skiprows=2,names=['flymiles','videogame','icecream','type'])
print(datadata[0:5])

mask= datadata.loc[:,'type']=='largeDoses'
print(datadata.loc[mask,:])

datadata.loc[datadata['videogame']>=10,'videogame']=10
print(datadata)