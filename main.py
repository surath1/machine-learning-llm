## from logchain_model import logger

from llm.logchain_model import logger
from llm.logchain_model.pipeline.stg_data_ingestion import DataIngestionPipeline
from llm.logchain_model.pipeline.vgg16_data_ingestion import Vgg16DataIngestionPipeline

logger.info("Welcome to LLM !!!")

STAGE_NAME = "data ingestion"

try:
    logger.info(f">>>>>> START: stage {STAGE_NAME} <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> END: stage {STAGE_NAME} <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "vgg16 data ingestion"

try:
    logger.info(f">>>>>> START: stage {STAGE_NAME} <<<<<<")
    obj = Vgg16DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> END: stage {STAGE_NAME} <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e