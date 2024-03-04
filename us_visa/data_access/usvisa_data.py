from us_visa.configuartion.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USVisaException
import pandas as pd
import sys
import numpy as np
from typing import Optional


class USVisaData:
    """
    This classs will help to import entire mongodb collection record as pandas dataframe object
    """
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USVisaException(e, sys) from e
    
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            if '_id' in df.columns.to_list():
                df = df.drop(columns=['_id'], axis = 1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise USVisaException(e, sys) from e