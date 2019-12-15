# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:45:59 2019

@author: FM
"""

#Após instalar o python na distribuição conda, para instalar os pacotes da API
#do Google Earth Engine, os seguintes comandos devem ser executados na linhas de
#comando do "Anaconda prompt", dentro do ambiente python ou ambiente python vir-
#tual de interesse:
conda install -c conda-forge earthengine-api
conda install -c conda-forge/label/gcc7 earthengine-api
conda install -c conda-forge/label/cf201901 earthengine-api

#Não está explicito na documentação, mas o pacote PIL é utilizado
#pela API então também deve ser instalado. O pacote pill, a partir
#do python 3.7 mudou de nome, agora "pillow".

conda install -c anaconda pillow