# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:25:09 2019

@author: FM
"""

import matplotlib.pyplot as plt
import netCDF4 as nc
import xarray as xr
import dask as da
#https://examples.dask.org/xarray.html
from dask.distributed import Client
from dask.diagnostics import ProgressBar
import xarray as xr
link ="http://www.esrl.noaa.gov/psd/thredds/dodsC/Aggregations/OISSThires/sst.mean.nc"
client = Client(n_workers=3, threads_per_worker=2, memory_limit='8GB')
ds = xr.open_dataset(link,chunks={'lat': 10, 'lon': 10, 'time': -1})



mont_data = ds.sel(time=slice('2017-01-01', '2019-01-01'))
mont_data_interp = mont_data.interpolate_na()
mont_mean = mont_data_interp.groupby('time.month').mean('time')

