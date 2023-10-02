import pandas
from Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator

class Ordenar_columnas(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        dFrame = dFrame.sort_values(by = ["CODI COMARCA", "DATA"])
        return dFrame