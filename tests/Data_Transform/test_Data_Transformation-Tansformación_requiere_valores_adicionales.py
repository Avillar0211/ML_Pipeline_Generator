from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas

dFrame = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))
dFrame = dFrame.dropna(axis = 0, how ='any')

try: 
    array =  ['Separar_colesterol', 'Ordenar_columnas', 'Agregar_LDL_discreto', 'Agregar_total_discreto']
    c = DataTransform(array)
    res = c.transform_data(dFrame)
except Exception as e:
    assert str(e) ==  'Revisa si alguna de las transformaciones requiere de valores adicionales para funcionar', 'No comprueba bien que en el Data Transform no se usen transformaciones que no sean compaitbles con la librería'
    exit



