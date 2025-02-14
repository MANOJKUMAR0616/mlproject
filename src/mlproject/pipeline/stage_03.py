from mlproject.components.model_training import ModelTrainer
from mlproject.config.configuration import ConfigurationManager

stage_name = "Model Training Stage"

class modeltrainingpipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_trainer_config()
        model_train = ModelTrainer(config = model_train_config)
        model_train.train()