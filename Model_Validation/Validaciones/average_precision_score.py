from sklearn.metrics import average_precision_score
from Model_Validation.Validaciones.Algorithm_Validator import Algorithm_Validator

class Average_precision_score(Algorithm_Validator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = average_precision_score(test_y, pred)
        return score
