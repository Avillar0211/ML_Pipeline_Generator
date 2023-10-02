from Model_Training.Algoritmos.Algorithm_Trainer import Algorithm_Trainer
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from scipy import stats

class RandomForestRegressorAL(Algorithm_Trainer):

    def __init__(self, properties):
        super().__init__()

        self.n_estimators = properties['n_estimators']
        self.random_state = properties['random_state']
        self.train_features = properties['train_features']
        self.train_labels = properties['train_labels']
        

    def train(self):

        print(self.n_estimators)
        print(self.random_state)

        rf = RandomForestRegressor(n_estimators=self.n_estimators, random_state=self.random_state)
        rf.fit(self.train_features, self.train_labels)

        return rf
