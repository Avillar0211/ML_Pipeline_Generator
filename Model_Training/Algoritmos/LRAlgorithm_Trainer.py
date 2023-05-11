from Algoritmos.Algorithm_Trainer import Algorithm_Trainer
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

        print(myfunc(10))

        print(slope)
        print(intercept)
        print(r)
        print(p)
        print (std_err)

        plt.scatter(x, y)
        plt.plot(x, mymodel)
        plt.show()



        return