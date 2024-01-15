import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator

class Filtrar_por_un_valor(single_data_transformator):

    def __init__(self, columnas):
        super().__init__()

    def transform(self, dFrame, columnas):
        dFrame = dFrame[(dFrame[columnas[0]] == columnas[1])]
        return dFrame