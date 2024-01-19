from sklearn.metrics import precision_score
from ML_Pipeline_Generator.Model_Validation.Validaciones.Single_ModelValidator import SingleModelValidator

class Precision_score(SingleModelValidator):
    """

    ADDITIONAL PROPERTIES:
    None

    """

    def __init__(self):
        super().__init__()
        
    def validate(test_y, pred):
        score = precision_score(test_y, pred)
        return score
