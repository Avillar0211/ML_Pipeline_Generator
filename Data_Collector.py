from Single_Data_Collector import single_data_collector
import pandas

class data_collector:
    def __init__(self):
        return
    
    def mergeDataSources(self, files):
        array = []
        c = single_data_collector()
        for file in files:
            dfaux = c.frame(file)
            array.append(dfaux)
        res = pandas.concat(array, ignore_index=True, sort=False)
        return pandas.DataFrame(res)
    