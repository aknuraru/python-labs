import psycopg2 as pgsql 
def many_users(): 
    try: 
        connection = pgsql.connect( 
            database="Phonebook", 
            user='postgres', 
            password='2007', 
            host='localhost', 
        ) 
        con = connection.cursor() 
        con.execute(r""" 
            CREATE OR REPLACE FUNCTION users(names TEXT[], surnames TEXT[], phones TEXT[]) RETURNS TEXT[] AS $$ 
            DECLARE 
                invalid_data TEXT[]; 
                i INT := 1; 
            BEGIN 
                WHILE i <= array_length(names, 1) LOOP 
                    IF length(phones[i]) <> 4 OR NOT phones[i] ~ '^\d+$' THEN 
                        invalid_data := array_append(invalid_data, names[i] || ' - ' || phones[i]); 
                    ELSE 
                        INSERT INTO phone_number (name, surname, number_value) VALUES (names[i], surnames[i], phones[i]); 
                    END IF; 
                    i := i + 1; 
                END LOOP; 
                RETURN invalid_data; 
            END; 
            $$ LANGUAGE plpgsql; 
        """) 
        connection.commit() 
        print("Successfully!") 
    except pgsql.Error as e: 
        print("Error while connecting to PostgreSQL", e) 
    finally: 
        if connection: 
            con.close() 
            connection.close() 
def users(names, surnames, phones): 
    try: 
        connection = pgsql.connect( 
            database="Phonebook", 
            user='postgres', 
            password='2007', 
            host='localhost', 
        ) 
        con = connection.cursor() 
 
        con.callproc('users', (names, surnames, phones)) 
        invalid_data = con.fetchone() 
        if invalid_data: 
            print("Invalid data:") 
            for data in invalid_data: 
                print(data) 
        else: 
            print("All users inserted successfully!") 
        connection.commit() 
    except pgsql.Error as e: 
        print("Error while connecting to PostgreSQL", e) 
    finally: 
        if connection: 
            con.close() 
            connection.close() 
many_users() 
names = ['Arai', 'Kendall','Kylie'] 
surnames = ['Hadid', 'Gomez','Ken'] 
phones = ['5766','2393','5233932'] 
users(names, surnames, phones)