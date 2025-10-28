import pymysql
from api.config import config

def get_db():
    conn = pymysql.connect(
        host=config["database"]["host"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["name"],
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return conn
