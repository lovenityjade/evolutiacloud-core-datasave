# api/utils/db.py - Database connection helper
import pymysql
from config import config

def get_db():
    """
    Returns a MySQL connection object
    """
    conn = pymysql.connect(
        host=config["database"]["host"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["name"],
        cursorclass=pymysql.cursors.DictCursor,  # results as dict
        autocommit=True
    )
    return conn
