from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
import pandas

aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 

try: 
    aux = FeatureEngineering([])
    data = aux.data_engineering(df)
except Exception as e:
    assert str(e) ==  'No se ha cargado ningúna Feature que se pueda aplicar dsobre los datos', 'No comprueba bien que en el Feature Engineering se estén intentando procesar un conjunto vacio de Features'
    exit


