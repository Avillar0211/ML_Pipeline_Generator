from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector
import pandas

try: 
    c = DataCollector([])
    res = c.readDataSources()
except Exception as e:
    assert str(e) ==  'No se ha cargado ningún archivo que leer', 'No avisa al usuairo que esta intentando leer un conjunto vacio de archivos'
    exit

