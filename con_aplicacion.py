from model_generator import pipeline_generator

model_generator = pipeline_generator()

model_generator.loadDataSources(['stroke_prediction_dataset_1.json', 'stroke_prediction_dataset_2.csv', 'stroke_prediction_dataset_3.html'])
dFrame = model_generator.readDataSources()

model_generator.loadCleaning(dFrame, ['Eliminar_duplicados','Eliminar_outliers','Valor_medio_en_nulos', 'Onehot_encoding'])
dFrame = model_generator.cleanData()

model_generator.loadTransformations(dFrame, ['Separar_colesterol', ['Ordenar_columnas', ['Patient Name', 'Age']], 'Agregar_LDL_discreto', 'Agregar_total_discreto'])
dFrame = model_generator.transformData()

model_generator.loadfeatures(dFrame, [['Eliminar_columnas',['Patient Name', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels', 'Cholesterol Levels', 'Symptoms']]])
model_generator.loadfeatures(dFrame, ['Missing_Value_Ratio', ['Data_Split', ['Diagnosis', 0.3]]])
data = model_generator.engineeringData()

train_x = data['train_x'] 
test_x = data['test_x'] 
train_y = data['train_y'] 
test_y = data['test_y'] 

propierties = {'max_iter': 10000, 'train_features' : train_x, 'train_labels': train_y}
model_generator.createModel("LogisticRegression", propierties)
model = model_generator.trainModel()

pred = model.predict(test_x)

model_generator.loadValidations(test_y, pred, ['Accuracy', 'Balanced_Accuracy_Score', 'Precision_score', 'Max_error', 'Mean_absolute_error'])
res = model_generator.validateModel()

print(res)