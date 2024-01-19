from ML_Pipeline_Generator.Model_Training.Model_Trainer import ModelTrainer

try:
    trainer = ModelTrainer(None,[])
    model = trainer.model_Training()
except Exception as e:
    assert str(e) ==  'No se ha cargado ningún Algoritmo que ejecutar', 'No comprueba bien que en el Model training se estén intentando entrenar sin un Algoritmo'
    exit

