import glob
import sys
import pandas

class single_data_collector:
    def __init__(self):
        return

    def frame(self, Filename):

        if(Filename.endswith('.json')):
            from Formatos.JSONDataCollector import read
        
        elif(Filename.endswith('.csv')):
            from Formatos.CSVDataCollector import read

        elif(Filename.endswith('.xml')):
            from Formatos.XMLDataCollector import read

        elif(Filename.endswith('.html')):
            from Formatos.HTMLDataCollector import read

        elif(Filename.endswith('.xls') or Filename.endswith('.xlsx') or Filename.endswith('.xlsm') or Filename.endswith('.xlsb')):
            from Formatos.ExcelDataCollector import read

        elif(Filename.endswith('.odf') or Filename.endswith('.ods') or Filename.endswith('.odt')):
            from Formatos.ExcelDataCollector import read
        
        return read(Filename)