from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))
dFrame = dFrame.dropna(axis = 0, how ='any')

try: 
    array =  ['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Transformación_que_no_existe', 'Agregar_total_discreto']
    c = DataTransform(array)
    res = c.data_transform(dFrame)
except Exception as e:
    assert str(e) ==  'La transformacion Transformación_que_no_existe no forma parte de la librería', 'No comprueba bien que en el Data Transform no se usen transformaciones que no sean compaitbles con la librería'
    exit



