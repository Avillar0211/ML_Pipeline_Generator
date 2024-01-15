from ML_Pipeline_Generator.Model_Training.Algoritmos.Algorithm_Trainer import Algorithm_Trainer
import pandas as pd 
from sklearn import linear_model

class LogisticRegressionAL(Algorithm_Trainer):

    def __init__(self, properties):
        super().__init__()

        self.max_iter = properties['max_iter']
        self.train_features = properties['train_features']
        self.train_labels = properties['train_labels']
        

    def train(self):

        rf = linear_model.LogisticRegression(max_iter = self.max_iter)
        rf.fit(self.train_features, self.train_labels)

        return rf
