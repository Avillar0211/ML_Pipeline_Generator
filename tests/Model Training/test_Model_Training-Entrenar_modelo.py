from sklearn.model_selection import train_test_split
import pandas
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from ML_Pipeline_Generator.Model_Training.Model_Trainer import ModelTrainer

aux = pandas.read_csv("stroke_prediction_dataset.csv")
dataset =  pandas.DataFrame(aux)

for x in aux: 
    if dataset[x].nunique() < 5: #miramos cuantas columnas tienen menos de 5 valores diferentes
        label_encoder = LabelEncoder() #creamos un objeto Label encoder
        dataset[x] = label_encoder.fit_transform(dataset[x]) #trnsformamos la columna string en un valor discretizado

dataset.drop(['Patient Name', 'Patient ID', 'Dietary Habits', 'Stress Levels', 'Blood Pressure Levels',
               'Cholesterol Levels', 'Symptoms'], axis = 'columns', inplace=True)
labels = dataset['Diagnosis']
x = dataset.drop ('Diagnosis', axis = 1)
train_x, test_x, train_y, test_y = train_test_split(x, labels, test_size = 0.2)


rf = linear_model.LogisticRegression(max_iter = 1000)
rf.fit(train_x, train_y)
pred = rf.predict(test_x)

trainer = ModelTrainer(None,[])
propierties = {'max_iter': 10000, 'train_features' : train_x, 'train_labels': train_y}
trainer.load_algorithm("LogisticRegression", propierties)
model = trainer.model_Training()

lib = model.predict(test_x)

assert (pred == lib).all(), 'El model Training no esta entrenando bien el algoritmo'

