from sklearn.model_selection import train_test_split
import pandas
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_score
from sklearn.metrics import max_error
from sklearn import linear_model
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

datos = []
aux = pandas.read_json("stroke_prediction_dataset_1.json")
Frame1 =  pandas.DataFrame(aux)
datos.append(Frame1)
aux = pandas.read_csv("stroke_prediction_dataset_2.csv")
Frame2 =  pandas.DataFrame(aux)
datos.append(Frame2)
with open("stroke_prediction_dataset_3.html", 'r', encoding="utf-8") as f:
            dfs = pandas.read_html(f.read())
Frame3 =  pandas.DataFrame(dfs[0])
datos.append(Frame3)
res = pandas.concat(datos, ignore_index=True, sort=False)
dataset = pandas.DataFrame(res)
dataset.drop('Unnamed: 0', inplace = True, axis = 1)


dataset = dataset.drop_duplicates() #eliminamos duplicados
aux = dataset.select_dtypes(include=np.number).columns.tolist() #guardamos las columnas que son numeros
for x in aux:
    mitjana = dataset[x].mean() #miramos el valor medio de x en el dataset
    desviacion = dataset[x].std() #miramos la desviacion media de x en el dataset
    min = mitjana - desviacion*5 #calculamos el minimo del intervalo restando la desviacion a la media
    max = mitjana + desviacion*5 #calculamos el maximo del intervalo sumando la desviacion a la media
    dataset.loc[dataset[x] < min, x] = mitjana #por cada valor menor al minimo ponemos la media
    dataset.loc[dataset[x] > max, x] = mitjana #por cada valor mayor al maximo sumamos la media
aux = dataset.select_dtypes(include=np.number).columns.tolist() #guardamos las columnas que son números
for x in aux:
    mitjana = dataset[x].mean() #calculamos el valor medio de x
    dataset[x].fillna(mitjana, inplace=True) #rellenamos los valores vacios con el valor medio
label_encoder = LabelEncoder() #creamos un objeto labelencoder
aux = dataset.select_dtypes(exclude=np.number).columns.tolist() #miramos las columnas con vlaor string
for x in aux: 
    if dataset[x].nunique() < 5: #miramos cuantas columnas tienen menos de 5 valores diferentes
        label_encoder = LabelEncoder() #creamos un objeto Label encoder
        dataset[x] = label_encoder.fit_transform(dataset[x]) #trnsformamos la columna string en un valor discretizado

dataset[['HDL', 'LDL']] = dataset['Cholesterol Levels'].str.split(',', expand=True) #separar colesterol
dataset['HDL'] = dataset['HDL'].str.replace('HDL: ', '')
dataset['LDL'] = dataset['LDL'].str.replace(' LDL: ', '')
dataset['HDL'] = pandas.to_numeric(dataset['HDL'])
dataset['LDL'] = pandas.to_numeric(dataset['LDL'])
dataset['Total Cholesterol'] = dataset.iloc[:, 22:24].sum(axis=1)
dataset = dataset.sort_values(by = ['Patient Name', 'Age']) #ordenar columnas
conditions = [ #agregar DLD discreto
    (dataset['LDL'] < 100),
    (dataset['LDL'] >= 100) & (dataset['LDL'] < 130),
    (dataset['LDL'] >= 130) & (dataset['LDL'] < 160),
    (dataset['LDL'] >= 160) & (dataset['LDL'] < 190),
    (dataset['LDL'] >= 190)
]
values = ['0', '1', '2', '3', '4'] #['Optimal', 'Near Optimal', 'Borderline High', 'High', 'Very High']
dataset['LDL_dis'] = np.select(conditions, values)
conditions = [ #agregar colesterl total discreto
    (dataset['Total Cholesterol'] < 200),
    (dataset['Total Cholesterol'] >= 200) & (dataset['Total Cholesterol'] < 240),
    (dataset['Total Cholesterol'] >= 240)
]
values = ['0', '1', '2'] #['Normal', 'Borderline High', 'High']
dataset['Total_Cholesterol_dis'] = np.select(conditions, values)


dataset.drop(['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels',
               'Cholesterol Levels', 'Symptoms'], axis = 'columns', inplace=True)
ratio = dataset.isnull().sum()/len(dataset)*100
print('Missing Value Ratio: ')
print(ratio)
labels = dataset['Diagnosis']
x = dataset.drop ('Diagnosis', axis = 1)
train_x, test_x, train_y, test_y = train_test_split(x, labels, test_size = 0.2)


rf = linear_model.LogisticRegression(max_iter = 1000)
rf.fit(train_x, train_y)
pred = rf.predict(test_x)

accuracy_score = accuracy_score(test_y, pred)
balanced_accuracy_score = balanced_accuracy_score(test_y, pred)
average_precision_score = average_precision_score(test_y, pred)
precision_score = precision_score(test_y, pred)
max_error = max_error(test_y, pred)
mean_absolute_error = mean_absolute_error(test_y, pred)

print('Accuracy score: ')
print(accuracy_score)
print('Balanced Acurracy Score: ')
print(balanced_accuracy_score)
print('Average Precision Score: ')
print(average_precision_score)
print('Precision Score: ')
print(precision_score)
print('Max Error: ')
print(max_error)
print('Mean Absolute Error: ')
print(mean_absolute_error)


