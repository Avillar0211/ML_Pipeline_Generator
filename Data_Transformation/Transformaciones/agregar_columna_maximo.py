import pandas
from Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator

class Agregar_columna_maximo(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        dFrame['MAXIM'] = dFrame.iloc[:, 12:35].max(axis=1)
        return dFrame