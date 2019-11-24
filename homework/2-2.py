import numpy as np
import pandas as pd

data=np.random.randint(10,99,size=(50,7))
print(data)

datadata=pd.DataFrame(data,columns=['a','b','c','d','e','f','g'])
print(datadata)
datadata.to_csv('1.csv',index = False)