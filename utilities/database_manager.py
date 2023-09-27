import pyodbc
from decouple import config


def get_connection():
    server = config('SQL_SERVER_NAME')
    database = config('SQL_DATABASE_NAME')
    username = config('SQL_ADMIN_LOGIN')
    password = config('SQL_ADMIN_PASSWORD')
    driver = '{ODBC Driver 17 for SQL Server}'

    connection = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +
                                ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    # Check if the table already exists
    cursor.execute(
        "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'DogImages'")

    # If the table doesn't exist, create it
    if not cursor.fetchone():
        create_table_query = """
        CREATE TABLE DogImages (
            ID INT PRIMARY KEY IDENTITY(1,1),
            ImageURL NVARCHAR(1000) NOT NULL
        );
        """

        cursor.execute(create_table_query)
        connection.commit()

    connection.close()


def save_to_azure(image_url):
    connection = get_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO DogImages (ImageURL) VALUES (?)"
    cursor.execute(insert_query, image_url)

    connection.commit()
    connection.close()
