from ML_Pipeline_Generator.Data_Cleaning.Procesos.Single_DataCleaner import SingleDataCleaner

class Eliminar_nulls(SingleDataCleaner):

    def __init__(self):
        super().__init__()

    def clean(self, dFrame):
        res = dFrame.dropna(axis = 0, how ='any') 
        return res