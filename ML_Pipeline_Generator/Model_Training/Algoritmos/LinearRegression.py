from ML_Pipeline_Generator.Model_Training.Algoritmos.Single_ModelTrainer import SingleModelTrainer
import pandas as pd 
from sklearn.linear_model import LinearRegression
import numpy 
import matplotlib.pyplot as plt
from scipy import stats

class LinearRegressionAL(SingleModelTrainer):

    def __init__(self, properties):
        super().__init__()

        self.x = properties['x']
        self.y = properties['y']
        self.Frame = properties['Frame']
        

    def train(self):

        x = self.Frame[self.x]
        y = self.Frame[self.y]

        new_x = numpy.array(x).reshape((-1, 1))

        mymodel = LinearRegression().fit(new_x,y)

        return mymodel
