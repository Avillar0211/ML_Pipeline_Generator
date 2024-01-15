from sklearn.metrics import balanced_accuracy_score
from ML_Pipeline_Generator.Model_Validation.Validaciones.Algorithm_Validator import Algorithm_Validator

class Balanced_Accuracy_Score(Algorithm_Validator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = balanced_accuracy_score(test_y, pred)
        return score
