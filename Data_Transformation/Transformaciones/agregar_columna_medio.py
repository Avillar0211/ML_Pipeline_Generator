import pandas
from Transformaciones.Single_Data_Transformator import single_data_transformator

class Agregar_columna_medio(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        dFrame['MITJANA_DIA'] = dFrame.iloc[:, 12:35].mean(axis=1)
        return dFrame