from sklearn.model_selection import train_test_split
import pandas
import numpy

class DataSplit():

    def split(self, dFrame, size):

        aux = dFrame.select_dtypes(include=[numpy.number])
        features = numpy.array(aux.iloc[:, :-1])
        labels = numpy.array(aux.iloc[:, -1])
        return train_test_split(features, labels, test_size = size)