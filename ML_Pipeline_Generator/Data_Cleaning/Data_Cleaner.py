from ML_Pipeline_Generator.Data_Cleaning.Procesos.eliminar_nulls import Eliminar_nulls 
from ML_Pipeline_Generator.Data_Cleaning.Procesos.eliminar_duplicados import Eliminar_duplicados
from ML_Pipeline_Generator.Data_Cleaning.Procesos.valor_medio_en_nulos import Valor_medio_en_nulos
from ML_Pipeline_Generator.Data_Cleaning.Procesos.eliminar_outliers import Eliminar_outliers
from ML_Pipeline_Generator.Data_Cleaning.Procesos.onehot_encoding import Onehot_encoding

class DataCleaner():
    def __init__(self, Procesos):
        self.singleDataCleaner = []
        for proc in Procesos:
            try:
                formatClassInstance = globals()[proc]
                self.singleDataCleaner.append((formatClassInstance))
            except: 
                raise Exception('El proceso de limpieza ' + proc + ' no forma parte de la librería')
        return
    
    def load_cleaning(self, Procesos):
        for proc in Procesos:
            try:
                formatClassInstance = globals()[proc]
                self.singleDataCleaner.append((formatClassInstance))
            except: 
                raise Exception('El proceso de limpieza ' + proc + ' no forma parte de la librería')
        return
    
    def clean_data(self, dFrame):
        if self.singleDataCleaner == []: 
            raise Exception('No se ha cargado ningún proceso para realizar la limpieza')
        for i in self.singleDataCleaner:
            res = i.clean(self, dFrame)
        return res
      
        