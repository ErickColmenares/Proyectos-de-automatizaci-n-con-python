"""
Este programa automatiza la creación de carpetas y subcarpetas
"""

import calendar    #importamos el módulo del calendario
from pathlib import Path   #importamos la librería para crear carpetas

meses_del_año=list(calendar.month_name[1:])  #Creamos una lista para los meses del año
dias_de_la_semana =['Día 1', 'Día 9', 'Día 18', 'Día 27']  #Creamos el número de días para las carpetas dentro de cada mes



for i, mes in enumerate(meses_del_año):  #A través de un bucle creamos las carpetas
    for dia in dias_de_la_semana:
        Path(f'2023/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True) #Utilizamemos la carpeta 2023 como la raíz
