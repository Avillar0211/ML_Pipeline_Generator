import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

class Ordenar_columnas(SingleDataTransformator):

    def __init__(self, columnas):
        super().__init__()

    def transform(self, dFrame, columnas):
        dFrame = dFrame.sort_values(by = [columnas[0], columnas[1]])
        return dFrame