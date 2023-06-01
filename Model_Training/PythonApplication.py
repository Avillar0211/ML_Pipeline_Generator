import Model_Trainer
from Model_Trainer import Model_Trainer
import numpy
import pandas

diccionario = {"x":"LATITUD", "y":"LONGITUD"}
aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
df['MAXIM'] = df.iloc[:, 12:35].max(axis=1)
#aux = df.loc[:,["LATITUD","LONGITUD"]]
c = Model_Trainer('LinearRegresionLibrary', diccionario)
model = c.model_Training(df)
#print(res)

x = numpy.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(model.predict(x))


print('ok')

