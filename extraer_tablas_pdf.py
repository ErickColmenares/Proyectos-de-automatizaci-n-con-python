"""
Extraer tabla de pdf
"""
import camelot #importamos la librería

tabla_3=camelot.read_pdf('tablas_prueba.pdf', pages=3)  #Obtenemos las tablas de la págna 3
tabla_3.export('tabla_prueba_3.csv', f='csv', compress=True )  #Las exportamos a un archivo .csv
tabla_3[0].to_csv('tabla_prueba_3.csv')