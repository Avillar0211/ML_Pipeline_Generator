from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas
from pandas.util.testing import assert_frame_equal
import numpy as np

array1 = ['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Agregar_total_discreto']
array2 = [['Filtrar_por_un_valor', ['Marital Status', 'Married']], 'Dividir_dummies']
aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)

df = df.dropna(axis = 0, how ='any')

c = DataTransform(array1)
c.load_transformations(array2)
res = c.transform_data(df)


aux = pandas.read_csv('stroke_prediction_dataset.csv')
dataset = pandas.DataFrame(aux)

dataset = dataset.dropna(axis = 0, how ='any')

dataset[['HDL', 'LDL']] = dataset['Cholesterol Levels'].str.split(',', expand=True) #separar colesterol
dataset['HDL'] = dataset['HDL'].str.replace('HDL: ', '')
dataset['LDL'] = dataset['LDL'].str.replace(' LDL: ', '')
dataset['HDL'] = pandas.to_numeric(dataset['HDL'])
dataset['LDL'] = pandas.to_numeric(dataset['LDL'])
dataset['Total Cholesterol'] = dataset.iloc[:, 22:24].sum(axis=1)
dataset = dataset.sort_values(by = ['Patient Name', 'Age']) #ordenar columnas
conditions = [ #agregar DLD discreto
    (dataset['LDL'] < 100),
    (dataset['LDL'] >= 100) & (dataset['LDL'] < 130),
    (dataset['LDL'] >= 130) & (dataset['LDL'] < 160),
    (dataset['LDL'] >= 160) & (dataset['LDL'] < 190),
    (dataset['LDL'] >= 190)
]
values = ['0', '1', '2', '3', '4'] #['Optimal', 'Near Optimal', 'Borderline High', 'High', 'Very High']
dataset['LDL_dis'] = np.select(conditions, values)
conditions = [ #agregar colesterl total discreto
    (dataset['Total Cholesterol'] < 200),
    (dataset['Total Cholesterol'] >= 200) & (dataset['Total Cholesterol'] < 240),
    (dataset['Total Cholesterol'] >= 240)
]
values = ['0', '1', '2'] #['Normal', 'Borderline High', 'High']
dataset['Total_Cholesterol_dis'] = np.select(conditions, values)
dataset = dataset[(dataset['Marital Status'] == 'Married')]
dataset = pandas.get_dummies(dataset)

assert_frame_equal(res,dataset, obj='La transformación de la librería no coincide con la transformación que debería estar haciendo')

