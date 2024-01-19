from sklearn.metrics import mean_absolute_error
from ML_Pipeline_Generator.Model_Validation.Validaciones.Single_ModelValidator import SingleModelValidator

class Mean_absolute_error(SingleModelValidator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = mean_absolute_error(test_y, pred)
        return score
