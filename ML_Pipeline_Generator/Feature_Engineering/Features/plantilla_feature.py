from ML_Pipeline_Generator.Feature_Engineering.Features.Single_DataFeature import SingleDataFeature

#Colocar el nombre de la clase
#El nombre de la clase sera el que se use para referenciarlo dentro de la libreria
class NombreDeLaFeature(SingleDataFeature):

    def __init__(self):
        super().__init__()


    def engineering(self, dFrame, columnas): #dFrame es el DataFrame que queremos transformar. Si se requieren más parametros colocar tras dFrame, ejemplo:columnas

        return dFrame #devolver dFrame tras haber aplicado la Feature