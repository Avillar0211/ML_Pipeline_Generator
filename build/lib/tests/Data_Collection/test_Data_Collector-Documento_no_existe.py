from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector
import pandas

try: 
    aux = ['noexiste.json', 'action.csv', 'crime.xlsx', 'family.html']
    c = DataCollector(aux)
    res = c.readDataSources()
except Exception as e:
    assert str(e) ==  'El archivo con nombre noexiste.json no se encuetra en el directorio', 'No indica que archivo es el que no encuentra'
    exit

