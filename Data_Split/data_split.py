from sklearn.model_selection import train_test_split
import pandas

def data_plit(dFrame):

    return train_test_split(dFrame, train_size=0.8, test_size=0.2)