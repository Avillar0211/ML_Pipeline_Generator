from Data_Processing.Procesos.Single_Data_Processor import single_data_processor
from sklearn.preprocessing import LabelEncoder
import numpy

class Onehot_encoding(single_data_processor):

    def __init__(self):
        super().__init__()

    def process(self, dFrame):
        aux = dFrame.select_dtypes(exclude=numpy.number).columns.tolist()
        for x in aux:
            print(dFrame[x].nunique())
            if dFrame[x].nunique() < 5:
                label_encoder = LabelEncoder()
                dFrame[x] = label_encoder.fit_transform(dFrame[x])
        
        return dFrame