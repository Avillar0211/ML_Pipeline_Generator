from Feature_engineer import FeatureEngineering
import pandas

aux = pandas.read_csv('contaminación_cortado.csv')
df = pandas.DataFrame(aux)
df = df.dropna(axis = 0, how ='any') 
df['MAXIM'] = df.iloc[:, 12:35].max(axis=1)
#aux = df.loc[:,["LATITUD","LONGITUD"]]

print(df.count(axis=1))

aux = FeatureEngineering(None, [])
aux.load_features(df,[['DataSplit', 0.2]])
train_x, test_x, train_y, test_y = aux.data_engineering()

print()
print(train_y.count(axis=1))



print('ok')

