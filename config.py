import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')
    # Use DATABASE_URL env var when available. Default to MariaDB (MySQL) using PyMySQL.
    # Example: export DATABASE_URL='mysql+pymysql://user:password@host:3306/fisiocontrol'
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost:3306/fisiocontrol'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
