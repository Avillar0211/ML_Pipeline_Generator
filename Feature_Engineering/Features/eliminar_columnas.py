from Feature_Engineering.Features.Single_Data_Feature import single_data_feature
import pandas
import numpy

class Eliminar_columnas(single_data_feature):

    def __init__(self):
        super().__init__()


    def engineering(self, dFrame, columnas):
        dFrame.drop(columnas, axis = 'columns', inplace=True)
        return dFrame