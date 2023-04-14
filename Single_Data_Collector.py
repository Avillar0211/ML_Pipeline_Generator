import glob
import sys
import pandas
from Formatos.JSONDataCollector import ClassJSONDataCollector
from Formatos.ExcelDataCollector import ClassExcelDataCollector
from Formatos.XMLDataCollector import ClassXMLDataCollector
from Formatos.CSVDataCollector import ClassCSVDataCollector

class single_data_collector:
    def __init__(self):
        self.formatos = []
        aux = ClassJSONDataCollector()
        self.formatos.append(('.json', aux))
        aux = ClassExcelDataCollector()
        self.formatos.append(('.xlsx', aux))
        aux = ClassCSVDataCollector()
        self.formatos.append(('.csv', aux))
        aux = ClassXMLDataCollector()
        self.formatos.append(('.xml', aux))

        return
    
    #def read(Filename):
        #pass

    def frame(self, Filename):

        for x in self.formatos:
            if(Filename.endswith(x[0])):
                aux = x[1]
                lectura = aux.read(Filename)
                return lectura
            
        print("Formato no compatible")
        return None
    
    def newFormat(self, extension, object):
        self.formatos.append((extension, object))