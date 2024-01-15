from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
import pandas

aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 

aux = FeatureEngineering(df, [['Eliminar_columnas',['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
aux.load_features(df, ['Missing_Value_Ratio', ['Data_Split', ['Diagnosis', 0.3]]])
data = aux.data_engineering()

with open('trainx.csv', 'w', encoding="utf-8") as output_file:
    output_file.write((data['train_x']).to_csv())

with open('trainy.csv', 'w', encoding="utf-8") as output_file:
    output_file.write((data['train_y']).to_csv())

print(data['train_x'].shape[0])
print(data['test_x'].shape[0])

print('ok')

