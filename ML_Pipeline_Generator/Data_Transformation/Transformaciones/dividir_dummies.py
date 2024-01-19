import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

class Dividir_dummies(SingleDataTransformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        newFrame = pandas.get_dummies(dFrame)
        return newFrame