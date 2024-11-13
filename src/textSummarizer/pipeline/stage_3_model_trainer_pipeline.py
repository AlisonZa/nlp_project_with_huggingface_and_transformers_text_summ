from src.textSummarizer.config.configuration import *

from src.textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainingPipeline():
    def __init__(self):
        pass
    
    def run_model_training(self):
        configuration_manager_obj = ConfigurationManager()
        model_trainer_config, model_trainer_params = configuration_manager_obj.get_model_trainer_config()
        model_trainer_obj = ModelTrainer(model_trainer_config, model_trainer_params)
        model_trainer_obj.train()


