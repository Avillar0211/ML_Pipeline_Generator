from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
import pandas

aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 

try: 
    aux = FeatureEngineering([['Eliminar_columnas',['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
    aux.load_features(['Feature_que_no_existe', ['Data_Split', ['Diagnosis', 0.3]]])
    res = aux.data_engineering(df)
except Exception as e:
    assert str(e) ==  'La Feature Feature_que_no_existe no forma parte de la librería', 'No comprueba bien que en el Feature Engineer no se usen Features que no sean compaitbles con la librería'
    exit



