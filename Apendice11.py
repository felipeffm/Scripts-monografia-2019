#!/usr/bin/env python
# coding: utf-8

# In[3]:


import xarray as xr


link = r"NOAA_NCDC_ERSST_v3b_SST.nc"
ds = xr.open_dataset(link)
sst = ds['sst']
lat = ds['lat']
lon = ds['lon']

ds_mm = ds.groupby('time.month').mean(dim='time')
ds_mm.sst.mean(dim='lon').transpose().plot.contourf(levels=12, vmin=-2, vmax=30)


# In[4]:


(ds_mm.sst.sel(month=1) - ds_mm.sst.sel(month=7)).plot(vmax=10)


# In[11]:


import xarray as xr
from matplotlib import pyplot as plt

lon_ponto = 50
lat_ponto = -20


link = r"D:\Google_Drive_v2\UFF - Bacharel\Monografia Felipe Miranda\NOAA_NCDC_ERSST_v3b_SST.nc"
ds = xr.open_dataset(link)
def remove_time_mean(x):
    return x - x.mean(dim='time')

ds_anom = ds.groupby('time.month').apply(remove_time_mean)

ds_anom.sst.sel(lon=lon_ponto, lat=lat_ponto).plot()


# In[16]:


ds_anom_mon = ds_anom.rolling(time=12, center=True).mean()
ds_anom_resample2 = ds_anom.resample(time='2Y').mean(dim='time')
#ds_anom_resample5 = ds_anom.resample(time='5Y').mean(dim='time')
ds_anom_resample10 = ds_anom.resample(time='10Y').mean(dim='time')
ds_anom_resample2.sst.sel(lon=lon_ponto, lat=lat_ponto).plot(marker='o', label='2 year resample')
#ds_anom_resample5.sst.sel(lon=lon_ponto, lat=lat_ponto).plot(marker='o', label='5 year resample')
ds_anom_resample10.sst.sel(lon=lon_ponto, lat=lat_ponto).plot(marker='o', label='10 year resample')
ds_anom_mon.sst.sel(lon=lon_ponto, lat=lat_ponto).plot(label='12 month rolling mean')
plt.legend()


# In[23]:


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
x = pd.DataFrame()
teste = pd.DataFrame()
y =(x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12)/12
teste['lat0'] =df_collection[1]['lat']
teste['lon0'] =df_collection[1]['lon']
def deslocar(df):
    df['lat']=df_collection[1]['lat']*-1
    df['lon']=df_collection[1]['lon']-360
    return df
x['lat']=df_collection[1]['lat']
x['lon']=df_collection[1]['lon']
x['sst']=y
teste['lat1'] =x['lat']
teste['lon1'] =x['lon']

teste


# In[20]:





# In[25]:



values = x['sst'].dropna()
import seaborn as sns
sns.distplot(values)


# In[26]:


lat_min=x['lat'].min()
lat_max=x['lat'].max()
lon_min=x['lon'].min()
lon_max=x['lon'].max()

limites = [[lat_min, lon_min],[lat_max ,lon_max ]] 
import matplotlib

cm = matplotlib.cm.get_cmap('cool')


def normalizar_cores(data):
    normed_data = (data - data.min()) / (data - data.min())
    return cm(normed_data)

color_data_intensity = normalizar_cores(b)


# In[11]:





# In[1]:





# In[ ]:




