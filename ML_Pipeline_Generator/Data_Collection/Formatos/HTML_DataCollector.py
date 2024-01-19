from ML_Pipeline_Generator.Data_Collection.Formatos.Single_DataCollector import SingleDataCollector
import pandas

class HTMLDataCollector(SingleDataCollector):

    def __init__(self):
        super().__init__()

    def read(self, Filename):
        with open(Filename, 'r', encoding="utf-8") as f:
            dfs = pandas.read_html(f.read())
        Frame =  pandas.DataFrame(dfs[0])
        return Frame
    