# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:49:02 2019

@author: FM
"""
#importar earth Engine
import ee
#importar ferramenta map client do Earth Engine
from ee import mapclient
#importar pacote usado internamente pelo earth engine



#Inicializando o Earth Engine
ee.Initialize()

# Get a download URL for an image.
image1 = ee.Image('CGIAR/SRTM90_V4')
path = image1.getDownloadUrl({
    #escala desejada
    'scale': 30,
    #codigo EPSG do sistema de coordenadas desejado
    'crs': 'EPSG:4326',
    #4 pontos do quadrado que se deseja recortar
    'region': '[[-120, 35], [-119, 35], [-119, 34], [-120, 34]]'
})
print (path)