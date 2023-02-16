from Single_Data_Collector import single_data_collector
import pandas

class data_collector:
    def __init__(self):
        aux = single_data_collector()

    def addSingleDataCollector(self, filename, format):
        aux = single_data_collector()
        return aux.read(filename,format)
    
    def mergeDataSources(self, files):
        array = []
        for file in files:
            dfaux = pandas.read_csv(file)
            array.append(dfaux)
        res = pandas.concat(array, ignore_index=True, sort=False)
        return pandas.DataFrame(res)
    