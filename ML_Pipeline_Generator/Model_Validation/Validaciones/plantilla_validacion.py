from ML_Pipeline_Generator.Model_Validation.Validaciones.Single_ModelValidator import SingleModelValidator

#Poner Nombre a la clase
#Sera el nombre con el que se referencia a la validacion desde la librería
class NombreDeLaValidacion(SingleModelValidator):

    def __init__(self):
        super().__init__()
        
    def validate(test, pred): #test es el dataframe donde esta el valor correcto y pred el valor que se ha predecido

        return #devolver el valor de la validación
