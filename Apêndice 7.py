# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:58:20 2019

@author: FM
"""
#Primeiro conectar ao FTP da NOAA e buscar todos os arquivos com a terminação .mon.mean
#Gerar uma lista, via terminal, com todos os arquivos da busca no Nautilus do Linux
CAMINHOS_NOAA = ['./ncep.reanalysis.derived/surface_gauss/dlwrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.10-200cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pres.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shum.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw200.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmin.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uflx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pevpr.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/weasd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.0-10cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/runof.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vwnd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uswrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnlf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vddsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uflx.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.0-10cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ugwd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/icec.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/skt.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/sfcr.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nbdsf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmax.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nbdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vflx.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shtfl.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnlf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/wspd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdlf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/prate.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uwnd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/prate.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cprat.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shum2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/lhtfl.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vbdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/air2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csusf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vgwd.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csusf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vflx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ugwd.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/lhtfl.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nddsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/gflux.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pevpr.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ulwrf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uwnd10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vwnd10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.300cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdsf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nswrs.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdlf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/skt.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shtfl.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.10-200cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nlwrs.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/runof.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vgwd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/gflux.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ulwrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/dswrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/air.2m.mon.mean.nc', './ncep.reanalysis.derived/tropopause/pres.tropp.mon.mean.nc', './ncep.reanalysis.derived/tropopause/air.mon.mean.nc', './ncep.reanalysis.derived/tropopause/air.tropp.mon.mean.nc', './ncep.reanalysis.derived/tropopause/pres.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.mct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/uswrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.lct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.mcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.hct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/csulf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.lcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/tcdc.eatm.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/dswrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/ulwrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.hcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/csusf.ntat.mon.mean.nc', './ncep.reanalysis.derived/sigma/chi.mon.mean.nc', './ncep.reanalysis.derived/sigma/psi.mon.mean.nc', './ncep.reanalysis.derived/sigma/vor.mon.mean.nc', './ncep.reanalysis.derived/sigma/div.mon.mean.nc', './ncep.reanalysis.derived/spectral/chi.mon.mean.nc', './ncep.reanalysis.derived/spectral/vor.mon.mean.nc', './ncep.reanalysis.derived/spectral/psi.mon.mean.nc', './ncep.reanalysis.derived/spectral/div.mon.mean.nc', './ncep.reanalysis.derived/pressure/shum.mon.mean.nc', './ncep.reanalysis.derived/pressure/vwnd.mon.mean.nc', './ncep.reanalysis.derived/pressure/hgt.mon.mean.nc', './ncep.reanalysis.derived/pressure/omega.mon.mean.nc', './ncep.reanalysis.derived/pressure/wspd.mon.mean.nc', './ncep.reanalysis.derived/pressure/pottmp.mon.mean.nc', './ncep.reanalysis.derived/pressure/rhum.mon.mean.nc', './ncep.reanalysis.derived/pressure/uwnd.mon.mean.nc', './ncep.reanalysis.derived/pressure/air.mon.mean.nc', './ncep.reanalysis.derived/surface/lftx4.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/pres.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_1000500.mon.mean.nc', './ncep.reanalysis.derived/surface/uwnd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/vwnd.mon.mean.nc', './ncep.reanalysis.derived/surface/lftx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/pr_wtr.eatm.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness.mon.mean.nc', './ncep.reanalysis.derived/surface/slp.mon.mean.nc', './ncep.reanalysis.derived/surface/pr_wtr.mon.mean.nc', './ncep.reanalysis.derived/surface/vwnd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/uwnd.mon.mean.nc', './ncep.reanalysis.derived/surface/wspd.mon.mean.nc', './ncep.reanalysis.derived/surface/air.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/rhum.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/air.mon.mean.nc', './ncep.reanalysis.derived/surface/omega.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_500200.mon.mean.nc', './ncep.reanalysis.derived/surface/wspd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/rhum.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_850500.mon.mean.nc', './ncep.reanalysis.derived/surface/pres.mon.mean.nc', './ncep.reanalysis.derived/surface/pottmp.sig995.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pevpr.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/skt.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/shtfl.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vgwd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/soilw.10-200cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/air.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.mct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tcdc.eatm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ulwrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ulwrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.hcb.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vflx.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ugwd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vwnd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/prate.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dswrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uflx.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uwnd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmax.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/icec.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.hct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/cprat.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/gflux.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/lhtfl.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.lcb.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/weasd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/runof.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmp.0-10cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dswrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uswrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmp.10-200cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uswrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/soilw.0-10cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/wspd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.lct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/shum.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dlwrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmin.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.mcb.mon.mean.nc', './ncep.reanalysis2.derived/surface/pr_wtr.eatm.mon.mean.nc', './ncep.reanalysis2.derived/surface/pres.sfc.mon.mean.nc', './ncep.reanalysis2.derived/surface/mslp.mon.mean.nc', './ncep.reanalysis2.derived/pressure/wspd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/vwnd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/uwnd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/rhum.mon.mean.nc', './ncep.reanalysis2.derived/pressure/omega.mon.mean.nc', './ncep.reanalysis2.derived/pressure/hgt.mon.mean.nc', './ncep.reanalysis2.derived/pressure/air.mon.mean.nc', './COBE2/sst.mon.mean.nc', './COBE2/icec.mon.mean.nc', './snowcover/snowcover.mon.mean.nc'] 
#a função abaixo gera os links ftp para download a partir dos caminhos, 
def get_path_files(NOAAs_paths, Parent_ftp_folder):
        path_file_list = []
        for x in CAMINHOS_NOAA:
                #tira o primeiro ponto da string
                x1 = x.split('.',1)[1]
                #Adiciona a palavra Dataset ao caminho
                x2 = Parent_ftp_folder + x1
                #Cria um dicionario com a path que o arquivo fica e o nome do arquivo
                x3 = x2.rsplit('/',1)
                path_file_list.append(x3)
        return path_file_list
        
a = get_path_files(CAMINHOS_NOAA, 'Datasets')


#depois de gerados os caminhos, executar o código abaixo para fazer download dos
#arquivos via FTP

#COMANDOS UTEIS
## ftp.retrlines('LIST') retorna as pastas dentro do ftp. 
#cwd('../') vai para o diretorio externo. 
#ftplib 'e nativa do python.

from ftplib import FTP  
import os.path
import pandas as pd
#a lista abaixo foi criada a partir do mecanismo de busca do terminal do ubuntu
#foi estabelecida uma conexao ftp, dentro da pasta datasets e o seguinte comando executado:
#find . -type f -name *"mon.mean.nc"
#copiei com o mouse a string que o comando retornou e fiz um parsing linuxem python para criar a lista abaixo:
CAMINHOS_NOAA = ['./ncep.reanalysis.derived/surface_gauss/dlwrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.10-200cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pres.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shum.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw200.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmin.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uflx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pevpr.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/weasd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.0-10cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/runof.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vwnd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uswrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnlf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vddsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uflx.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.0-10cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ugwd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/icec.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/skt.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/sfcr.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nbdsf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmax.2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nbdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vflx.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shtfl.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnlf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/wspd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdlf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/prate.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uwnd.10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/prate.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cprat.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shum2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/lhtfl.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vbdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/air2m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csusf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vgwd.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csusf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vflx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ugwd.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/lhtfl.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/cfnsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nddsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/gflux.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/pevpr.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ulwrf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdsf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/uwnd10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vwnd10m.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/tmp.300cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdsf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nswrs.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/csdlf.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/skt.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/shtfl.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/soilw.10-200cm.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/nlwrs.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/runof.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/vgwd.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/gflux.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/ulwrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/dswrf.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface_gauss/air.2m.mon.mean.nc', './ncep.reanalysis.derived/tropopause/pres.tropp.mon.mean.nc', './ncep.reanalysis.derived/tropopause/air.mon.mean.nc', './ncep.reanalysis.derived/tropopause/air.tropp.mon.mean.nc', './ncep.reanalysis.derived/tropopause/pres.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.mct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/uswrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.lct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.mcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.hct.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/csulf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.lcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/tcdc.eatm.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/dswrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/ulwrf.ntat.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/pres.hcb.mon.mean.nc', './ncep.reanalysis.derived/other_gauss/csusf.ntat.mon.mean.nc', './ncep.reanalysis.derived/sigma/chi.mon.mean.nc', './ncep.reanalysis.derived/sigma/psi.mon.mean.nc', './ncep.reanalysis.derived/sigma/vor.mon.mean.nc', './ncep.reanalysis.derived/sigma/div.mon.mean.nc', './ncep.reanalysis.derived/spectral/chi.mon.mean.nc', './ncep.reanalysis.derived/spectral/vor.mon.mean.nc', './ncep.reanalysis.derived/spectral/psi.mon.mean.nc', './ncep.reanalysis.derived/spectral/div.mon.mean.nc', './ncep.reanalysis.derived/pressure/shum.mon.mean.nc', './ncep.reanalysis.derived/pressure/vwnd.mon.mean.nc', './ncep.reanalysis.derived/pressure/hgt.mon.mean.nc', './ncep.reanalysis.derived/pressure/omega.mon.mean.nc', './ncep.reanalysis.derived/pressure/wspd.mon.mean.nc', './ncep.reanalysis.derived/pressure/pottmp.mon.mean.nc', './ncep.reanalysis.derived/pressure/rhum.mon.mean.nc', './ncep.reanalysis.derived/pressure/uwnd.mon.mean.nc', './ncep.reanalysis.derived/pressure/air.mon.mean.nc', './ncep.reanalysis.derived/surface/lftx4.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/pres.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_1000500.mon.mean.nc', './ncep.reanalysis.derived/surface/uwnd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/vwnd.mon.mean.nc', './ncep.reanalysis.derived/surface/lftx.sfc.mon.mean.nc', './ncep.reanalysis.derived/surface/pr_wtr.eatm.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness.mon.mean.nc', './ncep.reanalysis.derived/surface/slp.mon.mean.nc', './ncep.reanalysis.derived/surface/pr_wtr.mon.mean.nc', './ncep.reanalysis.derived/surface/vwnd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/uwnd.mon.mean.nc', './ncep.reanalysis.derived/surface/wspd.mon.mean.nc', './ncep.reanalysis.derived/surface/air.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/rhum.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/air.mon.mean.nc', './ncep.reanalysis.derived/surface/omega.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_500200.mon.mean.nc', './ncep.reanalysis.derived/surface/wspd.sig995.mon.mean.nc', './ncep.reanalysis.derived/surface/rhum.mon.mean.nc', './ncep.reanalysis.derived/surface/thickness_850500.mon.mean.nc', './ncep.reanalysis.derived/surface/pres.mon.mean.nc', './ncep.reanalysis.derived/surface/pottmp.sig995.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pevpr.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/skt.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/shtfl.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vgwd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/soilw.10-200cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/air.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.mct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tcdc.eatm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ulwrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ulwrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.hcb.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vflx.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/ugwd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/vwnd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/prate.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dswrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uflx.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uwnd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmax.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/icec.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.hct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/cprat.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/gflux.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/lhtfl.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.lcb.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/weasd.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/runof.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmp.0-10cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dswrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uswrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmp.10-200cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/uswrf.ntat.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/soilw.0-10cm.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/wspd.10m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.lct.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/shum.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/dlwrf.sfc.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/tmin.2m.mon.mean.nc', './ncep.reanalysis2.derived/gaussian_grid/pres.mcb.mon.mean.nc', './ncep.reanalysis2.derived/surface/pr_wtr.eatm.mon.mean.nc', './ncep.reanalysis2.derived/surface/pres.sfc.mon.mean.nc', './ncep.reanalysis2.derived/surface/mslp.mon.mean.nc', './ncep.reanalysis2.derived/pressure/wspd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/vwnd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/uwnd.mon.mean.nc', './ncep.reanalysis2.derived/pressure/rhum.mon.mean.nc', './ncep.reanalysis2.derived/pressure/omega.mon.mean.nc', './ncep.reanalysis2.derived/pressure/hgt.mon.mean.nc', './ncep.reanalysis2.derived/pressure/air.mon.mean.nc', './COBE2/sst.mon.mean.nc', './COBE2/icec.mon.mean.nc', './snowcover/snowcover.mon.mean.nc'] 


##########################O processo manual para conseguir os caminhos a partir da busca de uma string podia ser automatizado
##########################de repente mapear o nome dos arquivos associados a pastas
##########################e subpastas da NOAA em forma de dicionario e buscar com regex.
########################## o regex podia procurar na lista de acronimos aqui -> https://www.esrl.noaa.gov/psd/data/acronym/#L
 
#A partir da lista "Caminhos NOAA" a funcao abaixo retorna uma lista de listas com o arquivo e sua path no ftp
def get_path_files(NOAAs_paths, Parent_ftp_folder):
        path_file_list = []
        for x in CAMINHOS_NOAA:
                #tira o primeiro ponto da string
                x1 = x.split('.',1)[1]
                #Adiciona a palavra Dataset ao caminho
                x2 = Parent_ftp_folder + x1
                #Cria um dicionario com a path que o arquivo fica e o nome do arquivo
                x3 = x2.rsplit('/',1)
                path_file_list.append(x3)
        return path_file_list
 
#list of lists file<->paths       
ll_files_paths = get_path_files(CAMINHOS_NOAA, 'Datasets')

#file_path[0] = file directory path
#files_path[1] = file

ftp = FTP('ftp.cdc.noaa.gov')  
#colocar meu email aqui permite a NOAA me mandar e-mail se quiserem, mas nao 'e um campo obrigatorio.
ftp.login('anonymous','felipefm@id.uff.br')  
#lugar que vou salvar no meu hd antes de upar pro googledrive

armazenamento_local = 'home/fm_pc/Documents/Monografia_Modelo'
for i in range(0,10):
        os.chdir("..")

#loop passando por todos os arquivos
log_error = pd.DataFrame(columns = ['arquivo','ftp_path'])
arquivo = []
ftp_path = []
for file_path in ll_files_paths:
        armazenamento_local2 = armazenamento_local + '/'+ file_path[1]
        if os.path.exists(armazenamento_local2)==False:
                log_error['arquivo'] = arquivo
                log_error['ftp_path'] = ftp_path
                pass
                #print(file_path[1] + "ja esta baixada")
        else:
                try:
                        for i in range(0,10):
                                ftp.cwd('../')
                        ftp.cwd(file_path[0])
                        with open(armazenamento_local2, 'wb') as file: 
                        #file = open(armazenamento_local2, 'wb')
                                ftp.retrbinary("RETR" +" " +file_path[1], file.write, 8*1024)
                        #file.close
                except:
                        print('arquivo bixado --->'+file_path[0]+file_path[1])
                        arquivo.append(file_path[1])
                        ftp_path.append(file_path[0])
        if len(arquivo)>0:

