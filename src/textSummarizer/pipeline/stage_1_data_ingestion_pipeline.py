from src.textSummarizer.config.configuration import *

from src.textSummarizer.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass
    
    def run_training_pipeline(self):
        configuration_manager_obj = ConfigurationManager()
        data_ingestion_config = configuration_manager_obj.get_data_ingestion_config()
        data_ingestion_object = DataIngestion(data_ingestion_config)
        data_ingestion_object.initiate_data_ingestion()


