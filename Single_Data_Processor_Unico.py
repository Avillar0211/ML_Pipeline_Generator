import pandas

class single_data_processor:
    def __init__(self):
        return
    
    def eliminar_nulls(self, dataFrame):
        res = dataFrame.dropna(axis = 0, how ='any') 
        return res
    
    def eliminar_duplicados(self, dataFrame):
        res = dataFrame.drop_duplicates()
        return res
    
    def valor_medio_en_nulos(self, dataFrame):
        aux = []
        import numpy
        aux = dataFrame.select_dtypes(include=numpy.number).columns.tolist()

        for x in aux:
            mitjana = dataFrame[x].mean()
            dataFrame[x].fillna(mitjana, inplace=True)   


    def añadir_metodo(self, nombre, metodo):
        setattr(self, nombre, metodo)