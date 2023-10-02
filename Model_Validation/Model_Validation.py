from Model_Validation.Validaciones.accuracy import Accuracy
from Model_Validation.Validaciones.balanced_Accuracy_Score import Balanced_Accuracy_Score
from Model_Validation.Validaciones.max_error import Max_error
from Model_Validation.Validaciones.mean_absolute_error import Mean_absolute_error
from Model_Validation.Validaciones.precision_score import Precision_score
from Model_Validation.Validaciones.average_precision_score import Average_precision_score

class ModelValidator():
    def __init__(self, testy, pred, Validaciones):
        self.singleDataValidator = []
        self.testy = testy
        self.pred = pred
        for val in Validaciones:
            formatClassInstance = globals()[val]
            self.singleDataValidator.append(val, (formatClassInstance))
        return
    
    def load_validations(self, testy, pred, Validaciones):
        self.testy = testy
        self.pred = pred
        for val in Validaciones:
            formatClassInstance = globals()[val]
            self.singleDataValidator.append([val, (formatClassInstance)])
        return
    
    def validateModel(self):
        validations = []
        for i in self.singleDataValidator:
            validations.append([i[0], i[1].validate(self.testy, self.pred)])
        return validations
      