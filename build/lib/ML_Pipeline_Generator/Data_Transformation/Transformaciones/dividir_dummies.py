import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator

class Dividir_dummies(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        newFrame = pandas.get_dummies(dFrame)
        return newFrame