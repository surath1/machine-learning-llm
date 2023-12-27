from llm.logchain_model.config.config_manager import ConfigManager
from llm.logchain_model.components.vgg16_base_model import Vgg16BaseModel
from llm.logchain_model import logger

STAGE_NAME = "VGG16 Data Ingestion"

class Vgg16DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        vgg16_base_model_config = config.get_vgg16_base_model_config()
        vgg16_base_model = Vgg16BaseModel(config=vgg16_base_model_config)
        vgg16_base_model.get_base_model()
        vgg16_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> START: stage {STAGE_NAME} <<<<<<")
        obj = Vgg16DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>> END: stage {STAGE_NAME} <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

