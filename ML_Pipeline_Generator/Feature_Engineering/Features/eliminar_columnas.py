from ML_Pipeline_Generator.Feature_Engineering.Features.Single_DataFeature import SingleDataFeature
import pandas
import numpy

class Eliminar_columnas(SingleDataFeature):

    def __init__(self):
        super().__init__()


    def engineering(self, dFrame, columnas):
        dFrame.drop(columnas, axis = 'columns', inplace=True)
        return dFrame