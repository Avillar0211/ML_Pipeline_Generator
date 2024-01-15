from ML_Pipeline_Generator.Data_Processing.Procesos.eliminar_nulls import Eliminar_nulls 
from ML_Pipeline_Generator.Data_Processing.Procesos.eliminar_duplicados import Eliminar_duplicados
from ML_Pipeline_Generator.Data_Processing.Procesos.valor_medio_en_nulos import Valor_medio_en_nulos
from ML_Pipeline_Generator.Data_Processing.Procesos.eliminar_outliers import Eliminar_outliers
from ML_Pipeline_Generator.Data_Processing.Procesos.onehot_encoding import Onehot_encoding

class DataProcessor():
    def __init__(self, Procesos):
        self.singleDataProcesor = []
        for proc in Procesos:
            try:
                formatClassInstance = globals()[proc]
                self.singleDataProcesor.append((formatClassInstance))
            except: 
                raise Exception('El proceso de limpieza ' + proc + ' no forma parte de la librería')
        return
    
    def load_processes(self, Procesos):
        for proc in Procesos:
            try:
                formatClassInstance = globals()[proc]
                self.singleDataProcesor.append((formatClassInstance))
            except: 
                raise Exception('El proceso de limpieza ' + proc + ' no forma parte de la librería')
        return
    
    def data_processing(self, dFrame):
        if self.singleDataProcesor == []: 
            raise Exception('No se ha cargado ningún proceso para realizar la limpieza')
        for i in self.singleDataProcesor:
            res = i.process(self, dFrame)
        return res
      
        