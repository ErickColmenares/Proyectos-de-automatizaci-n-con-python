"""
Programa para trabajar con tabas de páginas web

"""

import pandas as pd   #Importamos librería
viviz=pd.read_html('https://es.wikipedia.org/wiki/Viviz')  #Guardamos tablas en una variable
tablas_viviz=len(viviz)  
tabla_discografia=viviz[1]  #Escogemos una tabla para trabajar