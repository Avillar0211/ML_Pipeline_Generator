from sklearn.model_selection import train_test_split
import pandas

def Missing_Value_Ratio(dFrame):

    '''
    Return Nulls value ratios over 5%
    '''

    null_columns = [ ]

    ratio_missing = dFrame.isnull().sum()/len(dFrame)*100
    columns = dFrame.columns

    for col in range(dFrame.columns.shape[0]):
        if (ratio_missing[col] >= 5):
            null_columns.append(columns[col])

    return null_columns