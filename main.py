from mlproject import logger
from mlproject.pipeline.stage_01 import trainingpipeline
from mlproject.pipeline.stage_02 import transformationpipeline
from mlproject.pipeline.stage_03 import modeltrainingpipeline
from mlproject.pipeline.stage_04 import modelevaluationpipeline


stage_name = "data ingestion pipeline"

try:
    logger.info(f">>>> stage {stage_name} started <<<<\n")
    data_ingestion = trainingpipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {stage_name} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise(e)

stage_name = "data transformation pipeline"

try:
    logger.info(f">>>> stage {stage_name} started <<<<\n")
    data_transformation = transformationpipeline()
    data_transformation.main()
    logger.info(f">>>> stage {stage_name} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise(e)

stage_name = "Model Training pipeline"

try:
    logger.info(f">>>> stage {stage_name} started <<<<\n")
    model_training = modeltrainingpipeline()
    model_training.main()
    logger.info(f">>>> stage {stage_name} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise(e)

stage_name = "Model Evaluation pipeline"

try:
    logger.info(f">>>> stage {stage_name} started <<<<\n")
    model_evaluation = modelevaluationpipeline()
    model_evaluation.main()
    logger.info(f">>>> stage {stage_name} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise(e)