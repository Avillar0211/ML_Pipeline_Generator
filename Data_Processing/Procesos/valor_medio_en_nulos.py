import pandas
import numpy
from Procesos.Single_Data_Processor import single_data_processor

class Valor_medio_en_nulos(single_data_processor):

    def __init__(self):
        super().__init__()

    def process(self, dFrame):
        aux = []
        aux = dFrame.select_dtypes(include=numpy.number).columns.tolist()

        for x in aux:
            mitjana = dFrame[x].mean()
            dFrame[x].fillna(mitjana, inplace=True)   

        return dFrame