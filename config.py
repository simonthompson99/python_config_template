import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    
    def __init__(self):
    
        self._db_name = os.getenv('DB_NAME')
        self._db_host = os.getenv('DB_HOST')
        self._db_port = os.getenv('DB_PORT') or 5432
        self._db_user = os.getenv('DB_USER')
        self._db_password = os.getenv('DB_PASSWORD')
    
    @property
    def db_conn_str(self):
    
        return f"postgresql+psycopg2://{self._db_user}:{self._db_password}@{self._db_host}:{self._db_port}/{self._db_name}"
        
