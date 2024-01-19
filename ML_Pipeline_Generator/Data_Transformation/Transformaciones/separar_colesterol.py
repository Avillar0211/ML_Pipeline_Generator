import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_DataTransformator import SingleDataTransformator

class Separar_colesterol(SingleDataTransformator):

    def __init__(self):
        super().__init__()

    def transform(self, dFrame):
        dFrame[['HDL', 'LDL']] = dFrame['Cholesterol Levels'].str.split(',', expand=True)
        dFrame['HDL'] = dFrame['HDL'].str.replace('HDL: ', '')
        dFrame['LDL'] = dFrame['LDL'].str.replace(' LDL: ', '')
        dFrame['HDL'] = pandas.to_numeric(dFrame['HDL'])
        dFrame['LDL'] = pandas.to_numeric(dFrame['LDL'])
        dFrame['Total Cholesterol'] = dFrame.iloc[:, 22:24].sum(axis=1)
        return dFrame