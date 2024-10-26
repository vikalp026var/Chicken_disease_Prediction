import os 
import urllib.request as request 
from pathlib import Path
import zipfile
from src.CnnClassifier import logging
from src.CnnClassifier.utils import get_size
from CnnClassifier.entity  import DataIngestionConfig




class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
            url=self.config.source_URL,
            filename=self.config.local_data_file
            )
            logging.info(f"{filename} download! with the following info:\n {headers}")
        else:
            logging.info(f"File already exits of size:{get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        