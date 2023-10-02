from model_generator import pipeline_generator
import numpy

model_generator = pipeline_generator()

model_generator.loadDataSources(['contaminacion_cortado1.csv', 'contaminacion_cortado2.json', 'contaminacion_cortado3.html'])
dFrame = model_generator.readDataSources()

model_generator.loadprocesses(dFrame, ['Eliminar_duplicados','Eliminar_outliers','Valor_medio_en_nulos', 'Onehot_encoding'])
dFrame = model_generator.processData()

model_generator.loadTransformations(dFrame, ['Ordenar_columnas','Agregar_columna_maximo','Agregar_columna_medio','Separar_fecha'])
dFrame = model_generator.transformData()

aux = dFrame.select_dtypes(include=[numpy.number])

train_x, test_x, train_y, test_y = model_generator.split_data(dFrame, 0.2)

propierties = {'n_estimators': 100, 'random_state' : 0, 'train_features' : train_x, 'train_labels': train_y}
model_generator.createModel("RandomForestRegressor", propierties)
model = model_generator.trainModel()

pred = model.predict(test_x)

model_generator.loadvalidations(test_y, pred, ['Accuracy', 'Balanced_Accuracy_Score', 'Average_precision_score', 'Precision_score', 'Max_error', 'Mean_absolute_error'])
res = model_generator.validateModel()

print(res)