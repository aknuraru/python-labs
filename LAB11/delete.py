import psycopg2 as pgsql
def delete_data_by_pattern(pattern):
    try:
        connection = pgsql.connect(
            database="Phonebook",
            user='postgres',
            password='2007',
            host='localhost',
        )
        con = connection.cursor()
        query = """
            DELETE FROM phone_number 
            WHERE name = %s 
            OR surname = %s 
            OR number_value = %s;
        """
        con.execute(query, (pattern, pattern, pattern))
        deleted_rows = con.rowcount
        print(f"Deleted {deleted_rows} rows.")
        connection.commit()
    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()
pat = input('Who do you want to delete? ')
delete_data_by_pattern(pat)