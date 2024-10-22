import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig
from mlProject import logger

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_data(self):
        try:
            
            data_frame = pd.read_csv(self.config.data_path)

            training_data, test_data = train_test_split(data_frame)

            training_data.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
            test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

            logger.info(f"Splited data into training and test data")
            logger.info(training_data.shape)
            logger.info(test_data.shape)

            print(training_data.shape)
            print(test_data.shape)

        except Exception as e:
            raise e