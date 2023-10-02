from sklearn.model_selection import train_test_split
import pandas

def Missing_Value_Ratio(dFrame):

    '''
    Return Nulls value ratios
    '''

    return dFrame.isnull().sum()/len(dFrame)*100
    