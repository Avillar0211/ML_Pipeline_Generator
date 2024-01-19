from ML_Pipeline_Generator.Model_Training.Model_Trainer import ModelTrainer

try:
    trainer = ModelTrainer('Algoritmo_no_existe',[])
    model = trainer.model_Training()
except Exception as e:
    assert str(e) ==  'El Algoritmo Algoritmo_no_existe no forma parte de la librería', 'No comprueba bien que en el Model training se haya puesto un algoritmo desconocido para la librería'
    exit

