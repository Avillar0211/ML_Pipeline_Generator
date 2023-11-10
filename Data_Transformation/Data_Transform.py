from Data_Transformation.Transformaciones.agregar_columna_medio import Agregar_columna_medio
from Data_Transformation.Transformaciones.agregar_columna_maximo import Agregar_columna_maximo
from Data_Transformation.Transformaciones.dividir_dataframe import Dividir_dataframe
from Data_Transformation.Transformaciones.filtrar_por_un_valor import Filtrar_por_un_valor
from Data_Transformation.Transformaciones.ordenar_columnas import Ordenar_columnas
from Data_Transformation.Transformaciones.dividir_dummies import Dividir_dummies
from Data_Transformation.Transformaciones.separar_fecha import Separar_fecha
from Data_Transformation.Transformaciones.separar_colesterol import Separar_colesterol
from Data_Transformation.Transformaciones.agregar_LDL_discreto import Agregar_LDL_discreto
from Data_Transformation.Transformaciones.agregar_total_discreto import Agregar_total_discreto

class DataTransform():
    def __init__(self, dFrame, Transformaciones):
        self.singleDataTransformator = []
        self.dFrame = dFrame
        for proc in Transformaciones:
            if isinstance(proc, list):
                formatClassInstance = globals()[proc[0]](proc[1])
                self.singleDataTransformator.append((formatClassInstance))
            else: 
                formatClassInstance = globals()[proc]
                self.singleDataTransformator.append(formatClassInstance)
        return
    
    def load_transformations(self, dFrame, Transformaciones):
        self.dFrame = dFrame
        for proc in Transformaciones:
            if isinstance(proc, list):
                formatClassInstance = globals()[proc[0]]
                self.singleDataTransformator.append([formatClassInstance, proc[1]])
            else: 
                formatClassInstance = globals()[proc]
                self.singleDataTransformator.append(formatClassInstance)
        return
    
    def data_transform(self):
        for i in self.singleDataTransformator:
            if isinstance(i, list):
                self.dFrame = i[0].transform(self, self.dFrame, i[1])
            else:
                self.dFrame = i.transform(self, self.dFrame)
        return self.dFrame
      
        