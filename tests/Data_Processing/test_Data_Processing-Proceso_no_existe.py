from ML_Pipeline_Generator.Data_Cleaning.Data_Cleaner import DataCleaner
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

try: 
    array = ['Eliminar_duplicados', 'Valor_medio_en_nulos', 'Proceso_que_no_existe', 'Eliminar_outliers', 'Onehot_encoding']
    c = DataCleaner(array)
    res = c.clean_data(dFrame)
except Exception as e:
    assert str(e) ==  'El proceso de limpieza Proceso_que_no_existe no forma parte de la librería', 'No comprueba bien que en el Data Processing no se usen formatos que no sean compaitbles con la librería'
    exit



