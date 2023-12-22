
from llm.logchain_model.config.config_manager import ConfigManager
from llm.logchain_model.components.data_ingestion import DataIngestion
from llm.logchain_model import logger

STAGE_NAME = "Data_Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> START: stage {STAGE_NAME} <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> END: stage {STAGE_NAME} <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


def test_ingestion():
    try:
        config = ConfigManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    except Exception as e:
        raise e
