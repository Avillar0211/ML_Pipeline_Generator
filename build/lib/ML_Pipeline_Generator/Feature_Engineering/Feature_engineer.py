from ML_Pipeline_Generator.Feature_Engineering.Features.Data_Split import Data_Split
from ML_Pipeline_Generator.Feature_Engineering.Features.Missing_Value_Ratio import Missing_Value_Ratio
from ML_Pipeline_Generator.Feature_Engineering.Features.eliminar_columnas import Eliminar_columnas

class FeatureEngineering():

    def __init__(self, Features):
        self.singleDataFeature = []
        for feat in Features:
            if isinstance(feat, list):
                formatClassInstance = globals()[feat[0]]
                self.singleDataFeature.append([formatClassInstance, feat[1]])
            else: 
                formatClassInstance = globals()[feat]
                self.singleDataFeature.append((formatClassInstance))
        return
    
    def load_features(self, Features):
        for feat in Features:
            if isinstance(feat, list):
                formatClassInstance = globals()[feat[0]]
                self.singleDataFeature.append([formatClassInstance, feat[1]])
            else: 
                formatClassInstance = globals()[feat]
                self.singleDataFeature.append((formatClassInstance))
        return
    
    def data_engineering(self, dFrame):
        for i in self.singleDataFeature:
            if isinstance(i, list):
                dFrame = i[0].engineering(self, dFrame, i[1])
            else:
                dFrame = i.engineering(self, dFrame)
        return dFrame
      