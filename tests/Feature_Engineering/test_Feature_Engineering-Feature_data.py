from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
from sklearn.model_selection import train_test_split
import pandas
import numpy as np

aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 

aux = FeatureEngineering([['Eliminar_columnas',['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
aux.load_features([ ['Data_Split', ['Diagnosis', 0.3]]])
data = aux.data_engineering(df)


aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
dataset = df.dropna(axis = 0, how ='any') 

dataset.drop(['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels',
               'Cholesterol Levels', 'Symptoms'], axis = 1)
labels = dataset['Diagnosis']
x = dataset.drop ('Diagnosis', axis = 1)
train_x, test_x, train_y, test_y = train_test_split(x, labels, test_size = 0.3)

assert data['train_x'].shape[0] == train_x.shape[0], 'Al hacer Feature Engineering no se aplican las Features como debería'
assert data['train_y'].shape[0] == train_x.shape[0], 'Al hacer Feature Engineering no se aplican las Features como debería'
assert data['test_x'].shape[0] == test_x.shape[0], 'Al hacer Feature Engineering no se aplican las Features como debería'
assert data['test_y'].shape[0] == test_y.shape[0], 'Al hacer Feature Engineering no se aplican las Features como debería'

