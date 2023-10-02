import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy

diccionario = {"x":"LATITUD", "y":"LONGITUD"}
aux = pandas.read_csv('contaminación_cortado.csv')

df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
df['MAXIM'] = df.iloc[:, 12:35].max(axis=1)

#print(len(df))

train, test = train_test_split(df, train_size=0.8, test_size=0.2)

x = train[diccionario['x']]
y = train[diccionario['y']]

new_x = numpy.array(x).reshape((-1, 1))

mymodel = LinearRegression().fit(new_x,y)

trainx = test[diccionario['x']]
trainy = test[diccionario['y']]

trainnew_x = numpy.array(trainx).reshape((-1, 1))

accuracy = mymodel.score(trainnew_x, trainy)

print("Accuracy: %.2f%%" % (accuracy*100.0))

#print(len(train), len(test))





#aux = df.loc[:,["LATITUD","LONGITUD"]]
#c = Model_Trainer('LinearRegresion', diccionario)
#res = c.model_Training(aux)
#print(res)


print('ok')

