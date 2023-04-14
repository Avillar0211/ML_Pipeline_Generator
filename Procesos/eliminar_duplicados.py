import pandas

class Eliminar_duplicados():

    def process(self, dFrame):
        res = dFrame.drop_duplicates()
        return res