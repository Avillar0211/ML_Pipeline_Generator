from ML_Pipeline_Generator.Data_Processing.Data_Processor import DataProcessor
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

try: 
    array = ['Eliminar_duplicados', 'Valor_medio_en_nulos', 'Proceso_que_no_existe', 'Eliminar_outliers', 'Onehot_encoding']
    c = DataProcessor(array)
    res = c.data_processing(dFrame)
except Exception as e:
    assert str(e) ==  'El proceso de limpieza Proceso_que_no_existe no forma parte de la librería', 'No comprueba bien que en el Data Processing no se usen formatos que no sean compaitbles con la librería'
    exit



