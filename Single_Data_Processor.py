import pandas
from Procesos.eliminar_nulls import Eliminar_nulls
from Procesos.eliminar_duplicados import Eliminar_duplicados
from Procesos.valor_medio_en_nulos import Valor_medio_en_nulos

class single_data_processor:
    def __init__(self):
        self.formatos = []
        aux = Eliminar_nulls()
        self.formatos.append(('eliminar_nulls', aux.process))
        aux = Eliminar_duplicados()
        self.formatos.append(('eliminar_duplicados', aux.process))
        aux = Valor_medio_en_nulos()
        self.formatos.append(('valor_medio_en_nulos', aux.process))

    def process(self, proceso, dFrame):
        for x in self.formatos:
            if(x[0] == proceso):
                aux = x[1]
                resultado = aux(dFrame)
                return resultado
            
        print("El proceso " + proceso + " esta mal escrito o no es compatible" )
        return None

    def newProcess(self, nombre, metodo):
        self.formatos.append((nombre, metodo))

