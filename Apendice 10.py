#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import xarray as xr
from folium.plugins import HeatMap

link = r"D:\Google_Drive_v2\UFF - Bacharel\Monografia Felipe Miranda\monthly_sst2.nc"
link2 = r"C:\Users\FM\domingo.nc"
ds = xr.open_dataset(link)
sst = ds['sst']
lat = ds['lat']
lon = ds['lon']


# In[2]:


#ds_mm = ds.groupby('time.month').mean(dim='time')


df_collection = {}
#Juntando os valores dos meses

for mon in range(int((ds.month.shape[0]))):
    df_collection[mon+1] = ds[dict(month=mon)].sst.to_dataframe()
    df_collection[mon+1].reset_index(inplace=True)
    #df_collection[mon+1] = df_collection[mon+1].dropna(axis=0, subset=['lat','lon', 'sst'])
    df_collection[mon+1] = df_collection[mon+1].drop(columns = {'month'})
    


# In[3]:


x1 = df_collection[1]['sst']
x2 = df_collection[2]['sst']
x3 = df_collection[3]['sst']
x4 = df_collection[4]['sst']
x5 = df_collection[5]['sst']
x6 = df_collection[6]['sst']
x7 = df_collection[7]['sst']
x8 = df_collection[8]['sst']
x9 = df_collection[9]['sst']
x10 = df_collection[10]['sst']
x11 = df_collection[11]['sst']
x12 = df_collection[12]['sst']
import pandas as pd
y = pd.DataFrame((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12)/12)
y['lat']=df_collection[1]['lat']+90
y['lon']=df_collection[1]['lon']
y['classif'] = pd.cut(x=y['lat'], bins=[0, 24,67, 113, 156,180], labels=['PolarS', 'TemperadaS', 'Tropical','TemperadaN','PolarN'])
y


# In[30]:


import seaborn as sns
sns.violinplot( y=x["sst"], x=y["classif"] )


# In[ ]:


sns.plt.show()


# In[41]:


# library
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
 

 
# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(y['lat'], y['lon'], y['sst'], cmap=plt.cm.jet, linewidth=0.1)
plt.show()
 


# In[45]:



ax.plot_contour(y['lat'], y['lon'], y['sst'])
plt.show()


# In[40]:



# Rotate it
ax.view_init(5, 5)
plt.show()


# In[36]:



# Other palette
ax.plot_trisurf(y['lat'], y['lon'], y['sst'], cmap=plt.cm.jet, linewidth=0.01)
plt.show()
 


# In[ ]:




