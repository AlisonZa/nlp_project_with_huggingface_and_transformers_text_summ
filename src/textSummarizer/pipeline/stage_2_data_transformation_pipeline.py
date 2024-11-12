from src.textSummarizer.config.configuration import *

from src.textSummarizer.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline():
    def __init__(self):
        pass
    
    def run_data_transformation(self):
        configuration_manager_obj = ConfigurationManager()
        data_transformation_config = configuration_manager_obj.get_data_transformation_config()
        data_transformation_object = DataTransformation(data_transformation_config)
        data_transformation_object.initiate_data_transformation()


