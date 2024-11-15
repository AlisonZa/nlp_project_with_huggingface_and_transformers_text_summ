from src.textSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.entity import *
from typing import Tuple


class ConfigurationManager:
    def __init__(self,
                config_path= CONFIG_FILE_PATH,
                params_path= PARAMS_FILE_PATH ):
        
        self.configurations = read_yaml(config_path)
        self.params = read_yaml(params_path)

        create_directories([self.configurations.artifacts_root]) # cria o /artifacts


    def get_data_ingestion_config(self)-> DataIngestionConfig:
        data_ingestion_config = self.configurations.data_ingestion
        
        create_directories([data_ingestion_config.root_dir]) # cria o /artifacts

        return data_ingestion_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig:
        data_transformation_config = self.configurations.data_transformation
        
        create_directories([data_transformation_config.root_dir]) # cria o /artifacts/data_transformation

        return data_transformation_config

    def get_model_trainer_config(self)-> Tuple[ModelTrainerConfig, ModelTrainerParams]:
        
        model_trainer_config = self.configurations.model_trainer
        model_trainer_params = self.params["TrainingArguments"]
    
        
        create_directories([model_trainer_config.root_dir]) # cria o /artifacts/model_trainer

        return model_trainer_config, model_trainer_params

