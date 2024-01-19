from ML_Pipeline_Generator.Model_Validation.Validaciones.accuracy import Accuracy
from ML_Pipeline_Generator.Model_Validation.Validaciones.balanced_Accuracy_Score import Balanced_Accuracy_Score
from ML_Pipeline_Generator.Model_Validation.Validaciones.max_error import Max_error
from ML_Pipeline_Generator.Model_Validation.Validaciones.mean_absolute_error import Mean_absolute_error
from ML_Pipeline_Generator.Model_Validation.Validaciones.precision_score import Precision_score
from ML_Pipeline_Generator.Model_Validation.Validaciones.average_precision_score import Average_precision_score

class ModelValidator():
    def __init__(self, Validaciones):
        self.singleDataValidator = []
        for val in Validaciones:
            try:
                formatClassInstance = globals()[val]
                self.singleDataValidator.append([val, (formatClassInstance)])
            except:
                raise Exception('La validacion ' + val + ' no forma parte de la librería')
        return
    
    def load_validations(self, Validaciones):
        for val in Validaciones:
            try:
                formatClassInstance = globals()[val]
                self.singleDataValidator.append([val, (formatClassInstance)])
            except:
                raise Exception('La validacion ' + val + ' no forma parte de la librería')
        return
    
    def validateModel(self, testy, pred):
        validations = []
        if self.singleDataValidator == []: 
            raise Exception('No se ha cargado ningúna validacion que se pueda aplicar sobre el modelo')
        for i in self.singleDataValidator:
            validations.append([i[0], i[1].validate(testy, pred)])
        return validations
      