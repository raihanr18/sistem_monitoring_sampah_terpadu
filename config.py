from os import getenv
from dotenv import load_dotenv

load_dotenv()  

class Config:
    SECRET_KEY = getenv('SECRET_KEY', 'default_secret_key') 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/sampah_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
