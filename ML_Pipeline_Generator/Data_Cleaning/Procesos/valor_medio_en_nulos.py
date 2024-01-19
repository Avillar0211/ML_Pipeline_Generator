import pandas
import numpy
from ML_Pipeline_Generator.Data_Cleaning.Procesos.Single_DataCleaner import SingleDataCleaner

class Valor_medio_en_nulos(SingleDataCleaner):

    def __init__(self):
        super().__init__()

    def clean(self, dFrame):
        aux = []
        aux = dFrame.select_dtypes(include=numpy.number).columns.tolist()

        for x in aux:
            mitjana = dFrame[x].mean()
            dFrame[x].fillna(mitjana, inplace=True)   

        return dFrame