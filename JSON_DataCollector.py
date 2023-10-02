from Data_Collection.Formatos.Single_DataCollector import SingleDataCollector
import pandas

class JSONDataCollector(SingleDataCollector):
   
    def __init__(self):
        super().__init__()
        
    def read(self, Filename):
        aux = pandas.read_json(Filename)
        Frame =  pandas.DataFrame(aux)
        return Frame