import Model_Trainer
from Model_Trainer import Model_Trainer
from sklearn.model_selection import train_test_split
import numpy
import pandas

aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
df['MAXIM'] = df.iloc[:, 12:35].max(axis=1)
#aux = df.loc[:,["LATITUD","LONGITUD"]]

features = numpy.array(df)
labels = numpy.array(df['MAXIM'])

train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size = 0.2)

diccionario = {"n_estimators":1000, "random_state":42, "train_features": train_x, "train_labels": train_y}

c = Model_Trainer('RandomForestRegressor', diccionario)
model = c.model_Training()
#print(res)

x = numpy.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(model.predict(x))


print('ok')

