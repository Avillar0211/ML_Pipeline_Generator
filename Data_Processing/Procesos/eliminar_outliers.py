import pandas
from Procesos.Single_Data_Processor import single_data_processor
import numpy

class Eliminar_outliers(single_data_processor):
    
    def __init__(self):
        super().__init__()
    
    def process(self, dFrame):
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