from ML_Pipeline_Generator.Data_Transformation.Transformaciones.filtrar_por_un_valor import Filtrar_por_un_valor
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.ordenar_columnas import Ordenar_columnas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.dividir_dummies import Dividir_dummies
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.separar_colesterol import Separar_colesterol
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.agregar_LDL_discreto import Agregar_LDL_discreto
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.agregar_total_discreto import Agregar_total_discreto

class DataTransform():
    def __init__(self, Transformaciones):
        self.singleDataTransformator = []
        for tran in Transformaciones:
            try:
                if isinstance(tran, list):
                    formatClassInstance = globals()[tran[0]]
                    self.singleDataTransformator.append([formatClassInstance, tran[1]])
                else: 
                    formatClassInstance = globals()[tran]
                    self.singleDataTransformator.append(formatClassInstance)
            except:
                raise Exception('La transformacion ' + tran + ' no forma parte de la librería')
        return
    
    def load_transformations(self, Transformaciones):
        for tran in Transformaciones:
            try:
                if isinstance(tran, list):
                    formatClassInstance = globals()[tran[0]]
                    self.singleDataTransformator.append([formatClassInstance, tran[1]])
                else: 
                    formatClassInstance = globals()[tran]
                    self.singleDataTransformator.append(formatClassInstance)
            except:
                raise Exception('La transformacion ' + tran + ' no forma parte de la librería')
        return
    
    def transform_data(self, dFrame):
        if self.singleDataTransformator == []: 
            raise Exception('No se ha cargado ningúna Transformación que se pueda aplicar dsobre los datos')
        for i in self.singleDataTransformator:
            if isinstance(i, list):
                dFrame = i[0].transform(self, dFrame, i[1])
            else:
                try:
                    dFrame = i.transform(self, dFrame)
                except TypeError:
                    raise Exception('Revisa si alguna de las transformaciones requiere de valores adicionales para funcionar')
        return dFrame
      
        