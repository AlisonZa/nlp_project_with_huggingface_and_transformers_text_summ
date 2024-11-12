import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.config.configuration import *

class DataIngestion():
    def __init__(self, 
                data_ingestion_config: DataIngestionConfig):

        self.data_ingestion_config = data_ingestion_config

    def download_data(self):
        """Downloads data from the source URL to the specified local path."""
        if not os.path.exists(self.data_ingestion_config.local_data_file):
            try:
                logger.info(f"Downloading data from {self.data_ingestion_config.source_URL}")
                request.urlretrieve(self.data_ingestion_config.source_URL, self.data_ingestion_config.local_data_file)
                logger.info(f"Data downloaded successfully to {self.data_ingestion_config.local_data_file}")
            except Exception as e:
                logger.error(f"Error downloading data: {e}")
                raise e
        else:
            logger.info(f"Data file already exists at {self.data_ingestion_config.local_data_file}")

    def extract_data(self):
        """Extracts the zip file to the specified directory."""
        if not os.path.exists(self.data_ingestion_config.unzip_dir):
            os.makedirs(self.data_ingestion_config.unzip_dir, exist_ok=True)
        
        try:
            with zipfile.ZipFile(self.data_ingestion_config.local_data_file, 'r') as zip_ref:
                logger.info(f"Extracting data to {self.data_ingestion_config.unzip_dir}")
                zip_ref.extractall(self.data_ingestion_config.unzip_dir)
                logger.info("Data extracted successfully.")
        except Exception as e:
            logger.error(f"Error extracting data: {e}")
            raise e

    def initiate_data_ingestion(self):
        """Orchestrates the download and extraction of data."""
        self.download_data()
        self.extract_data()