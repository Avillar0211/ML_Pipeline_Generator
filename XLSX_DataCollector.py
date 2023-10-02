from Data_Collection.Formatos.Single_DataCollector import SingleDataCollector
import pandas

class XLSXDataCollector(SingleDataCollector):

    def __init__(self):
        super().__init__()

    def read(self, Filename):
        aux = pandas.read_excel(Filename)
        Frame =  pandas.DataFrame(aux)
        return Frame
        