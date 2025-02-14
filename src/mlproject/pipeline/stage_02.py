from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager

stage_name = "Data Transformation Stage"

class transformationpipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_trans_config = config.get_data_transformation_config()
        data_trans = DataTransformation(config = data_trans_config)
        data_trans.train_test_split()