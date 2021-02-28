# Scripts de referência para TCC em Engenharia Ambiental na UFF. 

#### A Monografia consistiu em uma tentativa de unificar as principais fontes de dados ambientais climaticos do mundo a partir de seus metadados em um banco de dados MongoDB NoSQL. A partir dos metadados foi possível criar uma visualização da de uma localidade em um período prédeterminado via protocolo OpenDAP. Foi elaborado um draft em aplicação flask com backend em python estritamente com os dados da NOAA, hospedada no pythonanywhere para defesa. 

Pacotes utilizados: dask,earthengine-api, pillow, xarray, folium, ee, matplotlib, netCDF4, ftplib, geojson, pandas e pymongo

- 1 - Instalação de bibliotecas para download de datasets do Google Earth Engine;
- 2 - Download de raster disponível no Google Earth Engine em uma localidade aleatória;
- 3 - Geração de Mapa interativo com histórico de temperatura do oceano a nível global no Google Earth Engine;
- 4 - Referências globais para aquisição de dados ambientais mapeadas manualmente. 
- 5 - Abertura de arquivo grande com temperaturas do oceano, agora como fonte a NOAA, processamento paralelo em dask e realizando chunks. Em seguida alguns exemplos simples para cálculo de médias.
- 7 - Mapeamento do FTP da NOAA via python seguido do download em massa dos arquivos selecionados. 
- 8 - Abertura do arquivo, parser e upload para mongoDB
- 10 - Visualizações para análise de padrões de variação da temperatura superficial dos oceanos
- 11 - Visualizações para análise de padrões de variação da temperatura superficial dos oceanos
