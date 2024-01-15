from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas

array1 = ['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Agregar_total_discreto']
array2 = [['Filtrar_por_un_valor', ['Marital Status', 'Married']], 'Dividir_dummies']
aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)

df = df.dropna(axis = 0, how ='any')

c = DataTransform(array1)
c.load_transformations(array2)
res = c.data_transform(df)

print('ok')

