from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
import pandas

aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 

try: 
    aux = FeatureEngineering([['Eliminar_columnas',['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
    aux.load_features(['Data_Split'])
except Exception as e:
    print(e)
    assert str(e) ==  'Revisa si alguna de las Features requiere de valores adicionales para funcionar', 'No comprueba bien que en el Feature Engineer no se usen features que necesitem valores'
    exit



