from Data_Transformation.Transformaciones.agregar_columna_medio import Agregar_columna_medio
from Data_Transformation.Transformaciones.agregar_columna_maximo import Agregar_columna_maximo
from Data_Transformation.Transformaciones.dividir_dataframe import Dividir_dataframe
from Data_Transformation.Transformaciones.filtrar_por_un_valor import Filtrar_por_un_valor
from Data_Transformation.Transformaciones.ordenar_columnas import Ordenar_columnas
from Data_Transformation.Transformaciones.dividir_dummies import Dividir_dummies
from Data_Transformation.Transformaciones.separar_fecha import Separar_fecha

class DataTransform():
    def __init__(self, dFrame, Transformaciones):
        self.singleDataTransformator = []
        self.dFrame = dFrame
        for proc in Transformaciones:
            formatClassInstance = globals()[proc]
            self.singleDataTransformator.append((formatClassInstance))
        return
    
    def load_transformations(self, dFrame, Transformaciones):
        self.dFrame = dFrame
        for proc in Transformaciones:
            formatClassInstance = globals()[proc]
            self.singleDataTransformator.append((formatClassInstance))
        return
    
    def data_transform(self):
        for i in self.singleDataTransformator:
            self.dFrame = i.transform(self, self.dFrame)
        return self.dFrame
      
        