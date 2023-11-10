import pandas
import os.path
from Data_Collection.Formatos.JSON_DataCollector import JSONDataCollector
from Data_Collection.Formatos.HTML_DataCollector import HTMLDataCollector
from Data_Collection.Formatos.CSV_DataCollector import CSVDataCollector
from Data_Collection.Formatos.XLSX_DataCollector import XLSXDataCollector
from Data_Collection.Formatos.XML_DataCollector import XMLDataCollector

class DataCollector:
    def __init__(self, files):
        self.singleDataCollector = []
        for file in files:
            extension = os.path.splitext(file)[1]
            format = extension.upper()
            className = format.replace('.','')+'DataCollector'
            formatClassInstance = globals()[className]
            self.singleDataCollector.append((file, formatClassInstance))
        return

    def loadDataSources(self, files):
        for file in files:
            extension = os.path.splitext(file)[1]
            format = extension.upper()
            className = format.replace('.','')+'DataCollector'
            formatClassInstance = globals()[className]
            self.singleDataCollector.append((file, formatClassInstance))
        return
  
    def readDataSources(self):
        array = []
        for i in self.singleDataCollector:
            object = i[1]
            array.append(object.read(self, i[0]))

        res = pandas.concat(array, ignore_index=True, sort=False)
        final = pandas.DataFrame(res)
        final.drop('Unnamed: 0', inplace = True, axis = 1)
        return final