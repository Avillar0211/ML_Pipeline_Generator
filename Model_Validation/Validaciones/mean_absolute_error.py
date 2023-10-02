from sklearn.metrics import mean_absolute_error
from Model_Validation.Validaciones.Algorithm_Validator import Algorithm_Validator

class Mean_absolute_error(Algorithm_Validator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = mean_absolute_error(test_y, pred)
        return score
