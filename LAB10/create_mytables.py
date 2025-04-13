import psycopg2
from  config import load_config
def create_mytable():
    """ to create table in   PostgreSQL database(Phonebook)"""
    commands = """
        CREATE TABLE phone_number (
            name VARCHAR(255) NOT NULL,
            surname VARCHAR(255) NOT NULL,
            number_value VARCHAR(255) NOT NULL
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as db_connection:
            with db_connection.cursor() as db_cursor:
                db_cursor.execute(commands)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__ == '__main__':
    create_mytable()