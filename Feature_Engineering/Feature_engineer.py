from Feature_Engineering.Features.Data_Split import Data_Split
from Feature_Engineering.Features.Missing_Value_Ratio import Missing_Value_Ratio
from Feature_Engineering.Features.eliminar_columnas import Eliminar_columnas

class FeatureEngineering():

    def __init__(self, dFrame, Features):
        self.singleDataFeature = []
        self.dFrame = dFrame
        for feat in Features:
            if isinstance(feat, list):
                formatClassInstance = globals()[feat[0]]
                self.singleDataFeature.append([formatClassInstance, feat[1]])
            else: 
                formatClassInstance = globals()[feat]
                self.singleDataFeature.append((formatClassInstance))
        return
    
    def load_features(self, dFrame, Features):
        self.dFrame = dFrame
        for feat in Features:
            if isinstance(feat, list):
                formatClassInstance = globals()[feat[0]]
                self.singleDataFeature.append([formatClassInstance, feat[1]])
            else: 
                formatClassInstance = globals()[feat]
                self.singleDataFeature.append((formatClassInstance))
        return
    
    def data_engineering(self):
        for i in self.singleDataFeature:
            if isinstance(i, list):
                self.dFrame = i[0].engineering(self, self.dFrame, i[1])
            else:
                self.dFrame = i.engineering(self, self.dFrame)
        return self.dFrame
      