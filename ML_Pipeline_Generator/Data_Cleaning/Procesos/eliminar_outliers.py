import pandas
from ML_Pipeline_Generator.Data_Cleaning.Procesos.Single_DataCleaner import SingleDataCleaner
import numpy

class Eliminar_outliers(SingleDataCleaner):
    
    def __init__(self):
        super().__init__()
    
    def clean(self, dFrame):
        aux = []
        aux = dFrame.select_dtypes(include=numpy.number).columns.tolist()

        for x in aux:
            mitjana = dFrame[x].mean()
            desviacion = dFrame[x].std()
            min = mitjana - desviacion*5
            max = mitjana + desviacion*5
            dFrame.loc[dFrame[x] < min, x] = mitjana
            dFrame.loc[dFrame[x] > max, x] = mitjana

        return dFrame