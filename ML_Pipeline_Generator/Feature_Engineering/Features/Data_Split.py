from sklearn.model_selection import train_test_split
from ML_Pipeline_Generator.Feature_Engineering.Features.Single_DataFeature import SingleDataFeature
import numpy

class Data_Split(SingleDataFeature):

    def __init__(self):
        super().__init__()


    def engineering(self, dFrame, propiedades):
        labels = dFrame[propiedades[0]]
        x = dFrame.drop (propiedades[0], axis = 1)
        train_x, test_x, train_y, test_y = train_test_split(x, labels, test_size = propiedades[1])
        return {'train_x': train_x, 'test_x' : test_x, 'train_y' : train_y, 'test_y': test_y}

    