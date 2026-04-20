import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pymysql
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established %s",mydb)
        from sqlalchemy import create_engine

        engine = create_engine(
        "mysql+pymysql://root:SRNKCNrm%401000@localhost/college"
        )
        df = pd.read_sql("SELECT * FROM studentperformancefactors", engine)
        print(df.head())
        
        return df
    
    except Exception as ex:
        raise CustomException(ex,sys)