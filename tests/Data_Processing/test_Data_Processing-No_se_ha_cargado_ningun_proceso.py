from ML_Pipeline_Generator.Data_Cleaning.Data_Cleaner import DataCleaner
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

try: 
    array = []
    c = DataCleaner(array)
    res = c.clean_data(dFrame)
except Exception as e:
    assert str(e) ==  'No se ha cargado ningún proceso para realizar la limpieza', 'No comprueba bien que en el Data Transform se estén intentando procesar un conjunto vacio de transformaciones'
    exit



