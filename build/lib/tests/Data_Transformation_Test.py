from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
import pandas

array = ['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Agregar_total_discreto']
aux = pandas.read_csv('stroke_prediction_dataset.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
c = DataTransform(df, array)
res = c.data_transform()
with open('salidafusion.csv', 'w', encoding="utf-8") as output_file:
    output_file.write(res.to_csv())

print('ok')

