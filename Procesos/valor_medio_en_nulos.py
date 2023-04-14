import pandas
import numpy

class Valor_medio_en_nulos():

    def process(self, dFrame):
        aux = []
        aux = dFrame.select_dtypes(include=numpy.number).columns.tolist()

        for x in aux:
            mitjana = dFrame[x].mean()
            dFrame[x].fillna(mitjana, inplace=True)   