from mysql.connector import connect, Error
from cinema_config import DB_NAME, HOST, USER, PASSWORD


class DbConnectionError(Error):
    pass


def get_db_connection():
    try:
        connection = connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        print(f"Connected to DB: {DB_NAME}")
        return connection
    except Error as err:
        raise DbConnectionError(f"Failed to connect to the database: {err}")

# 7. Have db_utils file and use exception handling
