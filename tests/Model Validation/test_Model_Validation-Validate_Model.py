from sklearn.model_selection import train_test_split
import pandas
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from ML_Pipeline_Generator.Model_Validation.Model_Validation import ModelValidator
from sklearn.metrics import accuracy_score

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

accuracy_score = accuracy_score(test_y, pred)

rf = linear_model.LogisticRegression(max_iter = 1000)
rf.fit(train_x, train_y)

x = ModelValidator([])

x.load_validations(['Accuracy'])
res = x.validateModel(test_y , pred)

assert (res[0][1] == accuracy_score), 'El model validation no esta validadndo bien los modelos'



