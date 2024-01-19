from ML_Pipeline_Generator.Data_Collection.Formatos.Single_DataCollector import SingleDataCollector

#El nombre de la clase y el archivo debe ser el formato seguido por DataCollector para que el sistema pueda reconocerlo
#Ejemplo: si el formato fuese csv, sería el archivo CSV_DataCollector y la clase CSVDataCollector

class FormatoDataCollector(SingleDataCollector): 

    def __init__(self):
        super().__init__()

    def read(self, Filename): #Filename : nombre del archivo que se quiere leer
        #Introducir aqui la operacion para leer el formato
        return #devolver el objeto leído
        