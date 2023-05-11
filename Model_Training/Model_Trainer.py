from Algoritmos.BNAlgorithm_Trainer import BayesianNetwork
from Algoritmos.LRAlgorithm_Trainer import LinearRegresion

class Model_Trainer():
    def __init__(self, Alorithm, properties):
  
        self.formatClassInstance = globals()[Alorithm](properties)
        return
    
    def model_Training(self, dFrame):

        formatclass = self.formatClassInstance
        aux =  formatclass.train(dFrame)
        return aux
      
        