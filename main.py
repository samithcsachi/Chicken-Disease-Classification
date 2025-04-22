from CNNClassification import logger
from CNNClassification.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from CNNClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Prepare Base Model stage"

try:
    logger.info(f">>>>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
