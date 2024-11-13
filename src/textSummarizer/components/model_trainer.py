from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForSeq2Seq
import torch    
from datasets import load_from_disk
from src.textSummarizer.config.configuration import *
from src.textSummarizer.logging import logger
import os


class ModelTrainer:
    def __init__(self,
                 model_trainer_config: ModelTrainerConfig, 
                 model_trainer_params: ModelTrainerParams):
        """
        Initializes the ModelTrainer class with configuration details.

        Args:   
            model_trainer_config (ModelTrainerConfig): Configuration object containing the needed paths to perform the model training.
            model_trainer_params (ModelTrainerParams): Params object containing the needed params to perform the model training.
        """
        self.config = model_trainer_config
        self.params = model_trainer_params
        logger.info("ModelTrainer initialized with configuration and parameters.")

    def train(self):
        # Determine the device to use
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {device}")

        # Load tokenizer and model
        logger.info("Loading tokenizer and model.")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        logger.info("Tokenizer and model loaded successfully.")

        # Load the dataset
        logger.info(f"Loading dataset from {self.config.data_path}.")
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        logger.info("Dataset loaded successfully.")
        

        # Set up training arguments
        logger.info("Setting up training arguments.")
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            **self.params
        )
        logger.info("Training arguments set.")

        # Initialize the trainer
        logger.info("Initializing Trainer.")
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"]
        )

        # Start training
        logger.info("Starting training process.")
        trainer.train()
        logger.info("Training completed.")

        # Save model and tokenizer
        logger.info("Saving the trained model and tokenizer.")
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
        logger.info("Model and tokenizer saved successfully.")



