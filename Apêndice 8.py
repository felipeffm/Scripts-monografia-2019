# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:11:57 2019

@author: FM
"""

# coding: utf-8

# Código de leitura do netCDF 

# Estrutura do conjunto de dados:


#importa bibliotecas:
import numpy as np
import pandas as pd
import xarray as xr
import netCDF4
import geojson as geo
from geojson import Point
import os 
import pymongo 

path=r"D:\Google_Drive_v2\Big banco de dados _ compartilhado\Dados_Piloto"

#funcao que lista todos os arquivos netcdfs em uma pasta
def list_ncdf_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.nc' in file:
                files.append(os.path.join(r, file))
    return(files)
files = list_ncdf_files(path)


#Importa a Bilioteca pymongo
from pymongo import MongoClient, GEO2D
    
#Estabelece a conexão com o cliente local
client = MongoClient('localhost', 27017)
log_erros_importacao = []
#Seleciona o database local
db = client['local']
file = 'D:\\Google_Drive_v2\\Big banco de dados _ compartilhado\\Dados_Piloto\\nswrs.sfc.mon.mean.nc'
#files e uma lista com todos os caminhos dos netcdfs
def uploadfiles2mongo(files):
    for file in files:
        try:
            file_name = file.split(sep = "\\")[-1]
            netcdf = xr.open_dataset(file)
            
            #Atributos do DataArray (metadados)
            #netcdf_attrs = netcdf.attrs
            #netcdf_attrs
            #Dimensões do DataArray
            #netcdf_dims = netcdf.dims
            #netcdf_dims
            #Coordenadas do DataArray
            #netcdf_coords = netcdf.coords
            #netcdf_coords
            
            #Verifica os times do netCDF
            #netcdf.coords["time"]
            
            #Variáveis do DataArray
            #netcdf_vars = netcdf.data_vars
            
            #netcdf_vars
            
            #Seleciona apenas os 12 meses de dados, pois o DB limita a 16mb de dados sem GridFS
            meses = 12 #len(wspd.coords["time"])
            nc_netcdfs = []
            for i in range (meses):
                nc_netcdf = netcdf.isel(time=slice(i,i+1))
                nc_netcdfs.append(nc_netcdf)
            
            #print(len(nc_netcdfs) )
            
            #print(nc_netcdfs[11])
            
            #Verifica as dimensões
            #for i in nc_netcdfs:
                #print(i.data_vars)
            
            #seleciona a coleção de dados
            collection = db[file_name]
            
            
            for nc_netcdf in nc_netcdfs:
                nc_netcdf_dict = nc_netcdf.to_dict()
                collection.insert_one(nc_netcdf_dict)
            
            #Lista todas as collection
            
            print(file_name + " Adicionado como uma colecao")
        except:
            print("Erro no arquivo " + file_name)
            log_erros_importacao.append(file_name)
uploadfiles2mongo(files)            
db.list_collection_names()    
