# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:40 2019

@author: FM
"""

import xarray as xr


link = r"NOAA_NCDC_ERSST_v3b_SST.nc"
ds = xr.open_dataset(link)