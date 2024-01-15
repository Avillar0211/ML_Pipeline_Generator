from ML_Pipeline_Generator.Data_Processing.Data_Processor import DataProcessor
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

try: 
    array = []
    c = DataProcessor(array)
    res = c.data_processing(dFrame)
except Exception as e:
    assert str(e) ==  'No se ha cargado ningún proceso para realizar la limpieza', 'No comprueba bien que en el Data Transform se estén intentando procesar un conjunto vacio de transformaciones'
    exit



