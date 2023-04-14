from Single_Data_Processor import single_data_processor

class data_processor():
    def __init__(self):
        self.data_processor = single_data_processor()
        return
    
    def data_processing(self, processors, dFrame):
        for method in processors:
            dFrame = self.data_processor.process(method, dFrame)

        return dFrame

    def addProcess(self, nombre, metodo):
        self.data_processor.newProcess(nombre, metodo)
        print('El proceso ' + nombre + ' ha sido añadido')
      
        