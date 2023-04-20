from Procesos.Single_Data_Processor import single_data_processor

class Eliminar_nulls(single_data_processor):

    def __init__(self):
        super().__init__()

    def process(self, dFrame):
        res = dFrame.dropna(axis = 0, how ='any') 
        return res