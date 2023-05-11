import Model_Trainer
from Model_Trainer import Model_Trainer
import pandas

diccionario = {"x":"LATITUD", "y":"LONGITUD"}
aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
df['MAXIM'] = df.iloc[:, 12:35].max(axis=1)
c = Model_Trainer('LinearRegresion', diccionario)
res = c.model_Training(df)
print(res)


print('ok')

