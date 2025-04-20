import psycopg2 as pgsql
def update():
    try:
        connection = pgsql.connect(
            database="Phonebook",
            user='postgres',
            password='2007',
            host='localhost',
        )
        con = connection.cursor()
        con.execute("""
            CREATE OR REPLACE FUNCTION update_user(name_param TEXT, surname_param TEXT, phone_param TEXT) 
            RETURNS VOID AS 
            $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phone_number WHERE name = name_param OR surname = surname_param) THEN
                    UPDATE phone_number SET number_value = phone_param WHERE name = name_param OR surname = surname_param;
                ELSE
                    INSERT INTO phone_number (name, surname, number_value) VALUES (name_param, surname_param, phone_param);
                END IF;
            END;
            $$
            LANGUAGE plpgsql;
        """)
        connection.commit()
    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()
def update_user(name, surname, phone):
    try:
        connection = pgsql.connect(
            database="Phonebook",
            user='postgres',
            password='2007',
            host='localhost',
        )
        con = connection.cursor()
        con.callproc('update_user', (name, surname, phone))
        connection.commit()
    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()
update()
update_user('Aknur', 'Rys', '12345678')
update_user('Bella', 'Hadid', '21431569')
