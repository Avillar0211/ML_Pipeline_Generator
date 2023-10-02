from sklearn.model_selection import train_test_split
import pandas
import numpy
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

datos = []
aux = pandas.read_csv("contaminacion_cortado1.csv")
Frame1 =  pandas.DataFrame(aux)
datos.append(Frame1)
aux = pandas.read_json("contaminacion_cortado2.json")
Frame2 =  pandas.DataFrame(aux)
datos.append(Frame2)
with open("contaminacion_cortado3.html", 'r', encoding="utf-8") as f:
            dfs = pandas.read_html(f.read())
Frame3 =  pandas.DataFrame(dfs[0])
datos.append(Frame3)
res = pandas.concat(datos, ignore_index=True, sort=False)
dataset = pandas.DataFrame(res)


dataset = dataset.drop_duplicates() #eliminamos duplicados
aux = dataset.select_dtypes(include=numpy.number).columns.tolist() #guardamos las columnas que son numeros
for x in aux:
    mitjana = dataset[x].mean() #miramos el valor medio de x en el dataset
    desviacion = dataset[x].std() #miramos la desviacion media de x en el dataset
    min = mitjana - desviacion*5 #calculamos el minimo del intervalo restando la desviacion a la media
    max = mitjana + desviacion*5 #calculamos el maximo del intervalo sumando la desviacion a la media
    dataset.loc[dataset[x] < min, x] = mitjana #por cada valor menor al minimo ponemos la media
    dataset.loc[dataset[x] > max, x] = mitjana #por cada valor mayor al maximo sumamos la media
aux = dataset.select_dtypes(include=numpy.number).columns.tolist() #guardamos las columnas que son números
for x in aux:
    mitjana = dataset[x].mean() #calculamos el valor medio de x
    dataset[x].fillna(mitjana, inplace=True) #rellenamos los valores vacios con el valor medio
label_encoder = LabelEncoder() #creamos un objeto labelencoder
aux = dataset.select_dtypes(exclude=numpy.number).columns.tolist() #miramos las columnas con vlaor string
for x in aux: 
    if dataset[x].nunique() < 5: #miramos cuantas columnas tienen menos de 5 valores diferentes
        label_encoder = LabelEncoder() #creamos un objeto Label encoder
        dataset[x] = label_encoder.fit_transform(dataset[x]) #trnsformamos la columna string en un valor discretizado


dataset= dataset.sort_values(by = ["CODI COMARCA", "DATA"])
#dataset.reset_index(drop=True)
dataset['MAXIM'] = dataset.iloc[:, 12:35].max(axis=1)
dataset['MINIM'] = dataset.iloc[:, 12:35].min(axis=1)
dataset['MITJANA_DIA'] = dataset.iloc[:, 12:35].mean(axis=1)
dataset['DIA']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.day
dataset['MES']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.month
dataset['ANY']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.year
dataset.drop(['DATA'],axis=1,inplace=True)
dataset.drop('Unnamed: 0', inplace = True, axis = 1)
dataset.round()


aux = dataset.select_dtypes(include=[numpy.number])
features = numpy.array(aux.iloc[:, :-1])
labels = numpy.array(aux.iloc[:, -1])
train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size = 0.2)


rf = RandomForestRegressor(n_estimators=100, random_state=0)
rf.fit(train_x, train_y)
pred = rf.predict(test_x)


accuracy_score = accuracy_score(test_y, pred)
balanced_accuracy_score = balanced_accuracy_score(test_y, pred)
average_precision_score = average_precision_score(test_y, pred)
precision_score = precision_score(test_y, pred)
max_error = max_error(test_y, pred)
mean_absolute_error = mean_absolute_error(test_y, pred)

print(accuracy_score)
print(balanced_accuracy_score)
print(average_precision_score)
print(precision_score)
print(max_error)
print(mean_absolute_error)


