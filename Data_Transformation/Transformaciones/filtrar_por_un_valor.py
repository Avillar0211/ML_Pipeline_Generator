import pandas
from Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator

class Filtrar_por_un_valor(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        dFrame = dFrame[(dFrame["NOM ESTACIO"] == "Berga")]
        return dFrame