import pandas
import os.path
from ML_Pipeline_Generator.Data_Collection.Formatos.JSON_DataCollector import JSONDataCollector
from ML_Pipeline_Generator.Data_Collection.Formatos.HTML_DataCollector import HTMLDataCollector
from ML_Pipeline_Generator.Data_Collection.Formatos.CSV_DataCollector import CSVDataCollector
from ML_Pipeline_Generator.Data_Collection.Formatos.XLSX_DataCollector import XLSXDataCollector
from ML_Pipeline_Generator.Data_Collection.Formatos.XML_DataCollector import XMLDataCollector

class DataCollector:
    def __init__(self, files):
        self.singleDataCollector = []
        for file in files:
            extension = os.path.splitext(file)[1]
            format = extension.upper()
            className = format.replace('.','')+'DataCollector'
            try: 
                formatClassInstance = globals()[className]
                self.singleDataCollector.append((file, formatClassInstance))
            except:
                raise Exception('El formato ' + format + ' no forma parte de la librería')
        return

    def loadDataSources(self, files):
        for file in files:
            extension = os.path.splitext(file)[1]
            format = extension.upper()
            className = format.replace('.','')+'DataCollector'
            try: 
                className = format.replace('.','')+'DataCollector'
                formatClassInstance = globals()[className]
                self.singleDataCollector.append((file, formatClassInstance))
            except:
                raise Exception('El formato ' + format + ' no forma parte de la librería')
        return
  
    def readDataSources(self):
        array = []
        for i in self.singleDataCollector:
            object = i[1]
            try:
                array.append(object.read(self, i[0]))
            except: 
                raise Exception(('El archivo con nombre ' + i[0] + ' no se encuetra en el directorio'))
        final = []
        if array == []: 
            raise Exception('No se ha cargado ningún archivo que leer')
        else:
            res = pandas.concat(array, ignore_index=True, sort=False)
            final = pandas.DataFrame(res)
        #final.drop('Unnamed: 0', inplace = True, axis = 1)
        return final