import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.engine.base import Engine

host = os.getenv('hostname')
user = os.getenv('username')
password = os.getenv('password')
database = os.getenv('db_name')
port = os.getenv('port')

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

class SqlConnector:
    def __init__(self):
        self.engine = self.create_connection()

    def create_connection(self) -> Engine:
        """
        Creates a SQLAlchemy engine for a MySQL database.
        Parameters:
        - host (str): Hostname or IP of the MySQL server.
        - user (str): Username for the MySQL database.
        - password (str): Password for the MySQL database.
        - database (str): Name of the MySQL database to connect to.
        - port (int): Port number for the MySQL server. Defaults to 3306.
        Returns:
        - Engine: SQLAlchemy Engine object for the database connection.
        Raises:
        - SQLAlchemyError: If an error occurs while connecting to the MySQL database.
        """
        try:
            # Create the database engine
            engine = create_engine(DATABASE_URL, pool_pre_ping=True)
            logging.info(f"database connected to MySQL")
            print(f"database connected to MySQL")
            return engine
        except SQLAlchemyError as e:
            logging.error(f"Error while connecting to MySQL: {e}")
            print(f"Error while connecting to MySQL: {e}")
            raise


# conn = SqlConnector()
# print('connected', conn)