from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline


logger.info("Logging is implemented")


# Entrypoint
if __name__ == "__main__":
    data_ingestion_training_pipeline_obj = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline_obj.run_training_pipeline()

    data_transformation_training_pipeline_obj= DataTransformationTrainingPipeline()
    data_transformation_training_pipeline_obj.run_data_transformation()