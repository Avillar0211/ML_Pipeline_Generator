import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

class Filtrar_por_un_valor(SingleDataTransformator):

    def __init__(self, columnas):
        super().__init__()

    def transform(self, dFrame, columnas):
        dFrame = dFrame[(dFrame[columnas[0]] == columnas[1])]
        return dFrame