from Algoritmos.Algorithm_Trainer import Algorithm_Trainer
import pandas as pd 
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#from sklearn.model_selection import train_test_split 
#from sklearn.linear_model import LinearRegression 
#from sklearn import metrics
import matplotlib.pyplot as plt
from scipy import stats

class LinearRegresion(Algorithm_Trainer):

    def __init__(self, properties):
        super().__init__()

        self.x = properties['x']
        self.y = properties['y']
        self.eta = 0.5
        self.n_iterations = 1000
        

    def train(self, dFrame):

        x = dFrame[self.x]
        y = dFrame[self.y]

        slope, intercept, r, p, std_err = stats.linregress(x,y)

        def myfunc(x):
            return slope * x + intercept

        mymodel = list(map(myfunc, x))

        print(myfunc(0))

        print(slope)
        print(intercept)
        print(r)
        print(p)
        print (std_err)

        plt.scatter(x, y)
        plt.plot(x, mymodel)
        plt.show()

        return mymodel
    
    

        '''
        X = dFrame.drop([self.x,self.y],axis=1) 
        Y = dFrame[self.y] 
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)     

        lin_reg_model = LinearRegression() 
        lin_reg_model.fit(X_train,Y_train) 
        training_data_prediction = lin_reg_model.predict(X_train) 
        train_error_score = metrics.r2_score(Y_train, training_data_prediction) 
        print("R squared Error - Training : ", train_error_score) 
        '''



        return