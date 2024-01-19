from ML_Pipeline_Generator.Model_Validation.Model_Validation import ModelValidator
import pandas
from sklearn.model_selection import train_test_split
import pandas
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from ML_Pipeline_Generator.Model_Validation.Model_Validation import ModelValidator
from sklearn.metrics import accuracy_score

aux = pandas.read_csv("stroke_prediction_dataset.csv")
dataset =  pandas.DataFrame(aux)

for x in aux: 
    if dataset[x].nunique() < 5: 
        label_encoder = LabelEncoder() 
        dataset[x] = label_encoder.fit_transform(dataset[x])

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

try: 
    x = ModelValidator(['Accuracy', 'Balanced_Accuracy_Score', 'Validacion_que_no_existe', 'Precision_score', 'Max_error', 'Mean_absolute_error'])
    res = x.validateModel(test_y , pred)
except Exception as e:
    assert str(e) ==  'La validacion Validacion_que_no_existe no forma parte de la librería', 'No comprueba bien que en el Model Validation se estén intentando procesar un conjunto vacio de validaciones'
    exit


