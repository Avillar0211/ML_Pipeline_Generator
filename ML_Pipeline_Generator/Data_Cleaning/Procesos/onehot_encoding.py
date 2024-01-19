from ML_Pipeline_Generator.Data_Cleaning.Procesos.Single_DataCleaner import SingleDataCleaner
from sklearn.preprocessing import LabelEncoder
import numpy

class Onehot_encoding(SingleDataCleaner):

    def __init__(self):
        super().__init__()

    def clean(self, dFrame):
        aux = dFrame.select_dtypes(exclude=numpy.number).columns.tolist()
        for x in aux:
            if dFrame[x].nunique() < 5:
                label_encoder = LabelEncoder()
                dFrame[x] = label_encoder.fit_transform(dFrame[x])
        
        return dFrame