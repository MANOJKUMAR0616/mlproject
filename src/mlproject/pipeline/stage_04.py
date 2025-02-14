from mlproject.components.model_evaluation import ModelEvaluation
from mlproject.config.configuration import ConfigurationManager

stage_name = "Model Evaluation Stage"

class modelevaluationpipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config = model_eval_config)
        model_eval.save_results()