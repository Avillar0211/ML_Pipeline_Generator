from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector
import pandas

try: 
    aux = ['adventure.uwu', 'action.csv', 'crime.xlsx', 'family.html']
    c = DataCollector(aux)
    res = c.readDataSources()
except Exception as e:
    assert str(e) ==  'El formato .UWU no forma parte de la librería', 'No ha indica que formato es el que no conoce'
    exit

