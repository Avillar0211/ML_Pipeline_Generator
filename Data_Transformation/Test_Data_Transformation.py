import Data_Transform
from Data_Transform import DataTransform
import pandas

array = ['Agregar_columna_medio', 'Agregar_columna_maximo', 'Ordenar_columnas', 'Dividir_dummies']
aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
c = DataTransform(df, array)
res = c.data_transform()
with open('salidafusion.csv', 'w', encoding="utf-8") as output_file:
    output_file.write(res.to_csv())

print('ok')

