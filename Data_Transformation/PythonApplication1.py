import Data_Transform
from Data_Transform import data_transformator
import pandas

array = ['Agregar_columna_medio']
aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
c = data_transformator(df, array)
res = c.data_transform()
with open('salidafusion.csv', 'w', encoding="utf-8") as output_file:
    output_file.write(res.to_csv())

print('ok')

