from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

#Poner nombre de la transformacion
#Será el nombre con el que se referencie en la librería
class NombreDeLaTransformacion(SingleDataTransformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame, columnas): #dFrame es el DataFrame que queremos transformar. Si se requieren más parametros colocar tras dFrame, ejemplo:columnas
        
        return dFrame #devolver dFrame transformado