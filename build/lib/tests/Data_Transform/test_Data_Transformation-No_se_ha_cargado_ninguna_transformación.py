from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas

df = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))
df = df.dropna(axis = 0, how ='any')

try: 
    array = []
    c = DataTransform(array)
    res = c.data_transform(df)
except Exception as e:
    assert str(e) ==  'No se ha cargado ningúna Transformación que se pueda aplicar dsobre los datos', 'No comprueba bien que en el Data Processing se estén intentando procesar un conjunto vacio de procesos'
    exit


