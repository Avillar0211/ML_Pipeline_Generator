from Model_Training.Algoritmos.Bayesian_Network import BayesianNetworkAL
from Model_Training.Algoritmos.LinearRegression import LinearRegressionAL
from Model_Training.Algoritmos.RandomForestRegression import RandomForestRegressorAL
from Model_Training.Algoritmos.LogisticRegression import LogisticRegressionAL

class ModelTrainer():
    def __init__(self, Algorithm, properties):

        self.formatClassInstance = None

        if properties != []:
            self.formatClassInstance = globals()[Algorithm + 'AL'](properties)
        return
    
    def create_model(self, name, propierties):

        self.formatClassInstance = globals()[name + 'AL'](propierties)
    
    def model_Training(self):

        formatclass = self.formatClassInstance
        aux =  formatclass.train()
        return aux
      
        