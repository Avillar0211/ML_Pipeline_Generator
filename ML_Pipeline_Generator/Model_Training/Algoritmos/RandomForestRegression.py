from ML_Pipeline_Generator.Model_Training.Algoritmos.Single_ModelTrainer import SingleModelTrainer

#Poner nombre a la clase por el algoritmo que se va a implementar
#El nombre de la clase debe acabar en AL para ser reconocida por la librería
class NombreDelAlgoritmoAL(SingleModelTrainer):

    def __init__(self, properties):
        super().__init__()

        #Introducir la lectura de parametros para comprobar que se han enviado
        #Ejemplo : self.max_iter = properties['max_iter']
        #De esta manera se comprueba en ejecución que estan todos los parametros

    def train(self):

        #recojer parametros cargados. Ejemplo: self.max_iter

        return #devolver el modelo
