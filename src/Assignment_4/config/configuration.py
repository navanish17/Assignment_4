#configuration manager

from src.Assignment_4.constants import *
from src.Assignment_4.utils.common import read_yaml, create_directories
from src.Assignment_4.entity.config_entity import *


class ConfigurationManager:
    def __init__(
            
            self,
            config_filepath = Config_yaml_path,
            params_filepath = params_yaml_path,
            schema_filepath = schema_yaml_path 
    ):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(

            root_dir = config.root_dir,
            local_data_file = config.local_data_file
        )

        return data_ingestion_config