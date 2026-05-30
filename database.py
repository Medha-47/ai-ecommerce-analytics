import mysql.connector
import pandas as pd


def get_connection():
    """
    Create MySQL database connection
    """

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="krishna",
        database="ecommerce_ai"
    )

    return conn


def load_data():
    """
    Load orders table into Pandas DataFrame
    """

    conn = get_connection()

    query = """
    SELECT *
    FROM orders
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df