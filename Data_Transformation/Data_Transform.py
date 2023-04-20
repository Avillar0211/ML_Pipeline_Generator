from Transformaciones.agregar_columna_medio import Agregar_columna_medio
from Transformaciones.dividir_dataframe import Dividir_dataframe

class data_transformator():
    def __init__(self, dFrame, Procesos):
        self.singleDataTransformator = []
        self.dFrame = dFrame
        for proc in Procesos:
            formatClassInstance = globals()[proc]
            self.singleDataTransformator.append((formatClassInstance))
        return
    
    def data_transform(self):
        for i in self.singleDataTransformator:
            self.dFrame = i.transform(self, self.dFrame)
        return self.dFrame
      
        