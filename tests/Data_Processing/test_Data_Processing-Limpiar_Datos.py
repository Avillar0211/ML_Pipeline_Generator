from ML_Pipeline_Generator.Data_Cleaning.Data_Cleaner import DataCleaner
from pandas.util.testing import assert_frame_equal
import pandas
import numpy as np
from sklearn.preprocessing import LabelEncoder

array1 = ['Eliminar_duplicados', 'Valor_medio_en_nulos', 'Eliminar_nulls']
array2 = ['Eliminar_outliers', 'Onehot_encoding']
dFrame1 = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

df = pandas.DataFrame(dFrame1)
c = DataCleaner(array1)
c.load_cleaning(array2)
res = c.clean_data(df)

dataset = pandas.DataFrame(pandas.read_csv('stroke_prediction_dataset.csv'))

dataset = dataset.drop_duplicates() #eliminamos duplicados
aux = dataset.select_dtypes(include=np.number).columns.tolist() #guardamos las columnas que son números
for x in aux:
    mitjana = dataset[x].mean() #calculamos el valor medio de x
    dataset[x].fillna(mitjana, inplace=True) #rellenamos los va
datasets = dataset.dropna(axis = 0, how ='any') 
aux = dataset.select_dtypes(include=np.number).columns.tolist() #guardamos las columnas que son numeros
for x in aux:
    mitjana = dataset[x].mean() #miramos el valor medio de x en el dataset
    desviacion = dataset[x].std() #miramos la desviacion media de x en el dataset
    min = mitjana - desviacion*5 #calculamos el minimo del intervalo restando la desviacion a la media
    max = mitjana + desviacion*5 #calculamos el maximo del intervalo sumando la desviacion a la media
    dataset.loc[dataset[x] < min, x] = mitjana #por cada valor menor al minimo ponemos la media
    dataset.loc[dataset[x] > max, x] = mitjana #por cada valor mayor al maximo sumamos la media
aux = dataset.select_dtypes(exclude=np.number).columns.tolist() #miramos las columnas con vlaor string
for x in aux: 
    if dataset[x].nunique() < 5: #miramos cuantas columnas tienen menos de 5 valores diferentes
        label_encoder = LabelEncoder() #creamos un objeto Label encoder
        dataset[x] = label_encoder.fit_transform(dataset[x]) #trnsformamos la columna string en un valor discretizado
        dataset[x] = dataset[x].astype(int)

assert_frame_equal(res,dataset, obj='La limpieza de la librería no coincide con la limpieza que debería estar haciendo')



