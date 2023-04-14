from Single_Data_Collector import single_data_collector
import pandas

class data_collector:
    def __init__(self):
        self.data_collector = single_data_collector()
        return
    
    def mergeDataSources(self, files):
        array = []
        for file in files:
            dfaux = self.data_collector.frame(file)
            if(not dfaux.empty):
                array.append(dfaux)
        if (array != []):
            res = pandas.concat(array, ignore_index=True, sort=False)
            return pandas.DataFrame(res)
        return None
    
    def addFormat(self, extension, object):
        self.data_collector.newFormat(extension, object)
        print('El formato ' + extension + ' ha sido añadido')
    