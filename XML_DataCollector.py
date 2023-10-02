from Data_Collection.Formatos.Single_DataCollector import SingleDataCollector
import pandas

class XMLDataCollector(SingleDataCollector):

    def __init__(self):
        super().__init__()

    def read(self, Filename):
        aux = pandas.read_xml(Filename)
        Frame =  pandas.DataFrame(aux)
        return Frame
    