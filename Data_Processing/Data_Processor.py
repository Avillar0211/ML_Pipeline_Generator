from Data_Processing.Procesos.eliminar_nulls import Eliminar_nulls 
from Data_Processing.Procesos.eliminar_duplicados import Eliminar_duplicados
from Data_Processing.Procesos.valor_medio_en_nulos import Valor_medio_en_nulos
from Data_Processing.Procesos.eliminar_outliers import Eliminar_outliers
from Data_Processing.Procesos.onehot_encoding import Onehot_encoding

class DataProcessor():
    def __init__(self, dFrame, Procesos):
        self.singleDataProcesor = []
        self.dFrame = dFrame
        for proc in Procesos:
            formatClassInstance = globals()[proc]
            self.singleDataProcesor.append((formatClassInstance))
        return
    
    def load_processes(self, dFrame, Procesos):
        self.singleDataProcesor = []
        self.dFrame = dFrame
        for proc in Procesos:
            formatClassInstance = globals()[proc]
            self.singleDataProcesor.append((formatClassInstance))
        return
    
    def data_processing(self):
        for i in self.singleDataProcesor:
            self.dFrame = i.process(self, self.dFrame)
        return self.dFrame
      
        