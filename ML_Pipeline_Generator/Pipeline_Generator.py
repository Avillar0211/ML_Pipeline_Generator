from ML_Pipeline_Generator.Data_Collection.Data_Collector import DataCollector
from ML_Pipeline_Generator.Data_Cleaning.Data_Cleaner import DataCleaner
from ML_Pipeline_Generator.Data_Transformation.Data_Transform import DataTransform
from ML_Pipeline_Generator.Feature_Engineering.Feature_engineer import FeatureEngineering
from ML_Pipeline_Generator.Model_Training.Model_Trainer import ModelTrainer
from ML_Pipeline_Generator.Model_Validation.Model_Validation import ModelValidator

class pipeline_generator:
    def __init__(self):
        self.data_collector = DataCollector([])
        self.data_cleaner = DataCleaner([])
        self.data_transform = DataTransform([])
        self.feature_engineering = FeatureEngineering([])
        self.model_trainer = ModelTrainer(None, [])
        self.model_validator = ModelValidator([])

    def loadDataSources(self, files): 
        self.data_collector.loadDataSources(files)
        return
  
    def readDataSources(self):
        return self.data_collector.readDataSources()
    
    def loadCleaning(self, Procesos): 
        self.data_cleaner.load_cleaning(Procesos)
        return
    
    def cleanData(self, dFrame):
        return self.data_cleaner.clean_data(dFrame)
    
    def loadTransformations(self, Transformaciones):
        self.data_transform.load_transformations(Transformaciones)

    def transformData(self, dFrame):
        return self.data_transform.transform_data(dFrame)
    
    def loadFeatures(self, Features):
        self.feature_engineering.load_features(Features)

    def engineeringData(self, dFrame):
        return self.feature_engineering.data_engineering(dFrame)
    
    def loadAlgorithm(self, name, propierties):
        self.model_trainer.load_algorithm(name, propierties)

    def trainModel(self):
        return self.model_trainer.model_Training()

    def loadValidations(self, Validaciones):
        self.model_validator.load_validations(Validaciones)
        
    def validateModel(self, testy, pred):
        return self.model_validator.validateModel(testy, pred)