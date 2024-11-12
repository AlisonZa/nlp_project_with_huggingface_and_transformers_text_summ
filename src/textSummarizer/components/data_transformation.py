from transformers import AutoTokenizer
from datasets import load_from_disk
from src.textSummarizer.config.configuration import *

import os
from src.textSummarizer.logging import logger

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig):
        """
        Initializes the DataTransformation class with configuration details and tokenizer.

        Args:
            data_transformation_config (DataTransformationConfig): Configuration object containing
            paths and tokenizer information.
        """
        self.config = data_transformation_config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        """
        Converts a batch of examples into tokenized input features for a model.

        Args:
            example_batch (dict): A dictionary containing input and target texts for tokenization.

        Returns:
            dict: A dictionary with tokenized input features including 'input_ids', 'attention_mask',
                  and 'labels' (target token IDs).
        """
        # Tokenize the input dialogue with truncation to ensure length compatibility
        input_encodings = self.tokenizer(
            example_batch['dialogue'], max_length=1024, truncation=True
        )

        # Tokenize the target summary, using the tokenizer in target mode
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                example_batch['summary'], max_length=128, truncation=True
            )

        # Return the tokenized inputs with attention masks and target labels
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):
        """
        Loads the dataset, applies tokenization to each example, and saves the processed dataset.

        This method orchestrates the data transformation process by:
        1. Loading the dataset from disk.
        2. Applying the `convert_examples_to_features` function to each example.
        3. Saving the transformed dataset to a specified directory.
        """
        try:
            logger.info("Loading dataset from disk...")
            dataset_samsum = load_from_disk(self.config.data_path)

            logger.info("Transforming dataset with tokenization...")
            # Map the tokenization function across the dataset in a batched mode
            dataset_samsum_pt = dataset_samsum.map(
                self.convert_examples_to_features, batched=True
            )

            # Ensure the root directory exists before saving
            output_dir = os.path.join(self.config.root_dir, "samsum_dataset")
            os.makedirs(output_dir, exist_ok=True)

            logger.info(f"Saving processed dataset to {output_dir}...")
            dataset_samsum_pt.save_to_disk(output_dir)
            logger.info("Data transformation and saving complete.")

        except Exception as e:
            logger.error(f"Error in data transformation: {e}")
            raise e

    def initiate_data_transformation(self):
        """
        Orchestrates the entire data transformation process by calling the `convert` method.

        This method serves as the main entry point to perform all steps involved in data transformation,
        including loading, tokenizing, and saving the dataset.
        """
        try:
            logger.info("Initiating data transformation process...")
            self.convert()
            logger.info("Data transformation process completed successfully.")
        except Exception as e:
            logger.error(f"Data transformation process failed: {e}")
            raise e
