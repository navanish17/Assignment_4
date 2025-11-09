# components
import os
import numpy as np
import pandas as pd
from src.Assignment_4 import logger
from src.Assignment_4.utils.common import get_size
from src.Assignment_4.entity.config_entity import *


class Dataingestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    def data_file(self):
        local_path = self.config.local_data_file

        os.makedirs(os.path.dirname(local_path), exist_ok = True)

        print("Data infestion file made")