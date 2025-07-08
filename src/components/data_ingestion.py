import sys 
import os
import numpy as np
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    artifact_folder: str = os.path.join(artifact_folder)
    # str format
    
    
class DataIngestion:
    def __init__(self):
        self.data_ingesation_config= DataIngestionConfig()
        self.utils= MainUtils()
        
    def export_collection_as_dataframe(self,collection_name,db_name):
        try:
            mongo_client = MongoClient(MONGO_DB_URL)
            collection=mongo_client[db_name][collection_name]
            #now, dataframe me convert krege 
            df=pd.DataFrame(list(collection.find()))
            #removing id colum
            if "_id" in df.column.to_list():
                df=df.drop(columns=['_id'],axis=1)
                
            #handling missing value
            df.replace({"na":np.nan},inplace=True)
            
            return df
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def export_data_into_feature_store_file_path(self)-> pd.DataFrame:
        try:
            logging.info("Exporting data from mongoDb")
            raw_file_path = self.data_ingesation_config.artifact_folder
            os.makedirs(row_file_path,exist_ok=True)
            # agar phle se file exiust hai toh...error nhi dega
            sensor_data=self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME,
                db_name=MONGO_DATABASE_NAME
            )
            
            logging.info(f"saving exported data into feature store path:{raw_file_path}")
            feature_store_file_path=os.path.join(raw_file_path,'wafer_fault.csv')
            #convertin to data
            sensor_data.to_csv(feature_store_file_path,index=False)
        except Exception as e:
            raise CustomException(e,sys)
    
    
    def initiate_data_ingestion(self) -> Path:
        logging.info("Entered initiated_data_ingestion method of data_integration class ") 
        try:
            feature_store_file_path= self.export_data_into_feature_store_file_path()
            logging.info("got the data from mongodb")
            logging.info("exited initiative_data_ingestion method od data ingestion clas")
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys) from e
        
            