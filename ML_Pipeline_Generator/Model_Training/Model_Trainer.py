from ML_Pipeline_Generator.Model_Training.Algoritmos.Bayesian_Network import BayesianNetworkAL
from ML_Pipeline_Generator.Model_Training.Algoritmos.LinearRegression import LinearRegressionAL
from ML_Pipeline_Generator.Model_Training.Algoritmos.RandomForestRegression import RandomForestRegressorAL
from ML_Pipeline_Generator.Model_Training.Algoritmos.LogisticRegression import LogisticRegressionAL

class ModelTrainer():
    def __init__(self, Algorithm, properties):

        self.singleDataTrainer = None

        if Algorithm != None:
            try:
                self.singleDataTrainer = globals()[Algorithm + 'AL'](properties)
            except: 
                raise Exception('El Algoritmo ' + Algorithm + ' no forma parte de la librería')
        return
    
    def load_algorithm(self, Algorithm, propierties):

        try:
            self.singleDataTrainer = globals()[Algorithm + 'AL'](propierties)
        except: 
            raise Exception('El Algoritmo ' + Algorithm + ' no forma parte de la librería')
           
    def model_Training(self):
        if self.singleDataTrainer == None: 
            raise Exception('No se ha cargado ningún Algoritmo que ejecutar')
        formatclass = self.singleDataTrainer
        aux =  formatclass.train()
        return aux
      
        