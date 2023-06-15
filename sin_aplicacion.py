from sklearn.model_selection import train_test_split
import pandas
import numpy
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
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


dataset = dataset.drop_duplicates()
aux = dataset.select_dtypes(include=numpy.number).columns.tolist()
for x in aux:
    mitjana = dataset[x].mean()
    desviacion = dataset[x].std()
    min = mitjana - desviacion*5
    max = mitjana + desviacion*5
    dataset.loc[dataset[x] < min, x] = mitjana
    dataset.loc[dataset[x] > max, x] = mitjana
aux = dataset.select_dtypes(include=numpy.number).columns.tolist()
for x in aux:
    mitjana = dataset[x].mean()
    dataset[x].fillna(mitjana, inplace=True)  


dataset= dataset.sort_values(by = ["CODI COMARCA", "DATA"])
dataset['MAXIM'] = dataset.iloc[:, 12:35].max(axis=1)
dataset['MITJANA_DIA'] = dataset.iloc[:, 12:35].mean(axis=1)
dataset['DIA']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.day
dataset['MES']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.month
dataset['ANY']=pandas.to_datetime(dataset['DATA'],format='%d/%m/%Y').dt.year
dataset.drop(['DATA'],axis=1,inplace=True)
label_encoder = LabelEncoder()
columnas_string= dataset.select_dtypes(exclude=[numpy.number]).columns
for i in columnas_string:
    dataset[i] = label_encoder.fit_transform(dataset[i])

print("Label Encoded Data: ")


print(dataset.head())

features = numpy.array(dataset)
labels = numpy.array(dataset['MAXIM'])
train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size = 0.2)

rf = RandomForestRegressor(10, random_state=0)
rf.fit(train_x, train_y)

test_y.reshape(1, -1)
print(rf.score(test_y, test_x))

pred = rf.predict(test_x)
assessment = accuracy_score(test_y, pred)

print("ok")


