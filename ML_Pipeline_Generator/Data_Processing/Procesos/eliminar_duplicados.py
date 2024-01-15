from ML_Pipeline_Generator.Data_Processing.Procesos.Single_Data_Processor import single_data_processor

class Eliminar_duplicados(single_data_processor):

    def __init__(self):
        super().__init__()

    def process(self, dFrame):
        res = dFrame.drop_duplicates()
        return res