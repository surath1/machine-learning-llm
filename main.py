## from logchain_model import logger

from llm.logchain_model import logger
from llm.logchain_model.pipeline.stg_data_ingestion import DataIngestionPipeline

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