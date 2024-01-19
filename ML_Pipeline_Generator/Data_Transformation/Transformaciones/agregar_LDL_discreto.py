import numpy as np
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

class Agregar_LDL_discreto(SingleDataTransformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        conditions = [
            (dFrame['LDL'] < 100),
            (dFrame['LDL'] >= 100) & (dFrame['LDL'] < 130),
            (dFrame['LDL'] >= 130) & (dFrame['LDL'] < 160),
            (dFrame['LDL'] >= 160) & (dFrame['LDL'] < 190),
            (dFrame['LDL'] >= 190)
        ]

        values = ['0', '1', '2', '3', '4'] #['Optimal', 'Near Optimal', 'Borderline High', 'High', 'Very High']

        dFrame['LDL_dis'] = np.select(conditions, values)

        return dFrame