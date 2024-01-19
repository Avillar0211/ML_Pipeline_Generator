from ML_Pipeline_Generator.Pipeline_Generator import pipeline_generator

model_generator = pipeline_generator()

model_generator.loadDataSources(['stroke_prediction_dataset_1.json', 'stroke_prediction_dataset_2.csv', 'stroke_prediction_dataset_3.html'])
dFrame = model_generator.readDataSources()

model_generator.loadCleaning(['Eliminar_duplicados','Eliminar_outliers','Valor_medio_en_nulos', 'Onehot_encoding'])
dFrame = model_generator.cleanData(dFrame)

model_generator.loadTransformations(['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Agregar_total_discreto'])
dFrame = model_generator.transformData(dFrame)

model_generator.loadFeatures([['Eliminar_columnas',['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
model_generator.loadFeatures(['Missing_Value_Ratio', ['Data_Split', ['Diagnosis', 0.3]]])
data = model_generator.engineeringData(dFrame)

propierties = {'max_iter': 10000, 'train_features' : data['train_x'], 'train_labels': data['train_y'] }
model_generator.loadAlgorithm("LogisticRegression", propierties)
model = model_generator.trainModel()

pred = model.predict(data['test_x'])

model_generator.loadValidations(['Accuracy', 'Balanced_Accuracy_Score', 'Precision_score', 'Max_error', 'Mean_absolute_error'])
res = model_generator.validateModel(data['test_y'] , pred)
print(res)

