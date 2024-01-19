from ML_Pipeline_Generator.Data_Cleaning.Procesos.Single_DataCleaner import SingleDataCleaner

class Eliminar_duplicados(SingleDataCleaner):

    def __init__(self):
        super().__init__()

    def clean(self, dFrame):
        res = dFrame.drop_duplicates()
        return res