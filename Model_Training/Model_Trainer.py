from Algoritmos.BNAlgorithm_Trainer import BayesianNetwork
from Algoritmos.LinearRegression import LinearRegresion
from Algoritmos.LinearRegresionLibrary import LinearRegresionLibrary

class Model_Trainer():
    def __init__(self, Alorithm, properties):
  
        self.formatClassInstance = globals()[Alorithm](properties)
        return
    
    def model_Training(self, dFrame):

        formatclass = self.formatClassInstance
        aux =  formatclass.train(dFrame)
        return aux
      
        