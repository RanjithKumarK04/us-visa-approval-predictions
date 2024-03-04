import sys
import os
import pymongo
import certifi
from us_visa.exception import USVisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

ca = certifi.where()

class MongoDBClient:
    """
    class name: export data into feature store
    description: this method exports data into mongodb feature store as dataframe

    output: connection to mongodb database
    on failure: raises an exception
    """
    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Successfully connected to mongodb database: {database_name}")
        except Exception as e:
            raise USVisaException(e, sys)