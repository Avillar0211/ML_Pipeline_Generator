import pandas
from ML_Pipeline_Generator.Data_Transformation.Transformaciones.Single_Data_Transformator import single_data_transformator 

class Dividir_dataframe(single_data_transformator):

    def __init__(self):
        super().__init__()

    def process(self, dFrame):
        dades = dFrame.loc[:,['CODI EOI', 'DATA', 'MAGNITUD', 'CONTAMINANT', 'UNITATS', '01h', '02h', '03h','04h','05h','06h','07h','08h','09h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h','24h', 'MITJANA_DIA']]
        estacions = dFrame.loc[:,['CODI EOI', 'NOM ESTACIO', 'TIPUS ESTACIO', 'AREA URBANA', 'CODI INE', 'MUNICIPI', 'CODI COMARCA', 'NOM COMARCA', 'ALTITUD', 'LONGITUD', 'Georeferència']]
        return [dades,estacions]