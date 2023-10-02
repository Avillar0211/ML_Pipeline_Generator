from sklearn.metrics import max_error
from Model_Validation.Validaciones.Algorithm_Validator import Algorithm_Validator

class Max_error(Algorithm_Validator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = max_error(test_y, pred)
        return score
