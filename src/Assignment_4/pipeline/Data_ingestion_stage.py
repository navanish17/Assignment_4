#pipeline
from src.Assignment_4.constants import *
from src.Assignment_4.utils.common import read_yaml, create_directories
from src.Assignment_4.entity.config_entity import *
from src.Assignment_4.config.configuration import *
from src.Assignment_4.components.Data_ingestion import *

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Dataingestion(config = data_ingestion_config)
        data_ingestion.data_file()