import pandas

class Eliminar_nulls():

    def process(self, dFrame):
        res = dFrame.dropna(axis = 0, how ='any') 
        return res