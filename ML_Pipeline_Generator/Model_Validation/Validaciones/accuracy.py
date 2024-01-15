from sklearn.metrics import accuracy_score
from ML_Pipeline_Generator.Model_Validation.Validaciones.Algorithm_Validator import Algorithm_Validator

class Accuracy(Algorithm_Validator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = accuracy_score(test_y, pred)
        return score