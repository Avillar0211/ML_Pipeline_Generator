from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator
import numpy as np

class Agregar_total_discreto(single_data_transformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        conditions = [
            (dFrame['Total Cholesterol'] < 200),
            (dFrame['Total Cholesterol'] >= 200) & (dFrame['Total Cholesterol'] < 240),
            (dFrame['Total Cholesterol'] >= 240)
        ]

        values = ['0', '1', '2'] #['Normal', 'Borderline High', 'High']

        dFrame['Total_Cholesterol_dis'] = np.select(conditions, values)
        return dFrame