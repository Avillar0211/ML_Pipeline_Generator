from Data_Collection.Data_Collector import DataCollector
from Data_Processing.Data_Processor import DataProcessor
from Data_Transformation.Data_Transform import DataTransform
from Feature_Engineering.Feature_engineer import FeatureEngineering
from Model_Training.Model_Trainer import ModelTrainer
from Model_Validation.Model_Validation import ModelValidator

class pipeline_generator:
    def __init__(self):
        self.data_collector = DataCollector([])
        self.data_processor = DataProcessor(None, [])
        self.data_transform = DataTransform(None, [])
        self.feature_engineering = FeatureEngineering(None, [])
        self.model_trainer = ModelTrainer(None, [])
        self.model_validator = ModelValidator(None,None, [])

    def loadDataSources(self, files): 
        self.data_collector.loadDataSources(files)
        return
  
    def readDataSources(self):
        return self.data_collector.readDataSources()
    
    def loadCleaning(self, dFrame, Procesos): 
        self.data_processor.load_processes(dFrame, Procesos)
        return
    
    def cleanData(self):
        return self.data_processor.data_processing()
    
    def loadTransformations(self, dFrame, Transformaciones):
        self.data_transform.load_transformations(dFrame, Transformaciones)

    def transformData(self):
        return self.data_transform.data_transform()
    
    def loadfeatures(self, dFrame, Features):
        self.feature_engineering.load_features(dFrame, Features)

    def engineeringData(self):
        return self.feature_engineering.data_engineering()
    
    def createModel(self, name, propierties):
        self.model_trainer.create_model(name, propierties)

    def trainModel(self):
        return self.model_trainer.model_Training()

    def loadValidations(self, testy, pred, Validaciones):
        self.model_validator.load_validations(testy, pred, Validaciones)
        
    def validateModel(self):
        return self.model_validator.validateModel()