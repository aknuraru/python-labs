import psycopg2 as pgsql
def search_records(pattern):
    try:
        connection = pgsql.connect(
            database="Phonebook",
            user='postgres',
            password='2007',
            host='localhost',
        )
        con = connection.cursor()
        query = "SELECT * FROM phone_number WHERE name LIKE %s OR surname LIKE %s OR number_value LIKE %s"
        con.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
        records = con.fetchall()
        return records
    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()
pattern = input("Search: ...")
same_records = search_records(pattern)
print("Same Records:")
for record in same_records:
    print(record)