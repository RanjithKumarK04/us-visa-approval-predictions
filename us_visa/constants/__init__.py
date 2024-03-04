import os
from datetime import date

DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"

pipeline_name: str = 'usvisa'
artifact_dir: str = 'artifact'

model_file_name = 'model.pkl'

target_column = 'case_status'
current_year = date.today().year
preprocessing_object_file_name = 'preprocessing.pkl'

file_name: str = 'usvisa.csv'
train_file_name: str = 'train.csv'
test_file_name: str = 'test.csv'
schema_file_path = os.path.join("config", "schema.yaml")

"""
Data Ingestion related constant start with data_ingestion var name
"""
data_ingestion_collection_name: str = 'visa_data'
data_ingestion_dir_name: str = 'data_ingestion'
data_ingestion_feature_store_dir: str = 'feature_store'
data_ingestion_ingested_dir: str = 'ingested'
data_ingestion_train_test_split_ratio: float = 0.2