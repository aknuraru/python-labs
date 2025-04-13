import csv
import psycopg2
db_connection=psycopg2.connect(
    host='localhost',
    database='Phonebook',
    user='postgres',
    password='2007',
    port='5432'
)
db_cursor=db_connection.cursor()
array=[]
choice=input("type 1 for inserting csv or 2 for inserting from console")
if choice=='1':
    #insert using csv file
    with open('PhoneBook.csv') as f:
        f_read=csv.reader(f, delimiter=',')
        for row in f_read:
            row[0] = str(row[0].strip(','))
            array.append(row)
    postgress_insert_query="""INSERT INTO phone_number VALUES (%s,%s,%s) RETURNING *;"""
    for i in array:
        db_cursor.execute(postgress_insert_query, i)
    db_connection.commit()
    print("successfully !!")
    db_connection.close()
elif choice=='2':
    #  user name, phone from console
    firstname = str(input("Name: "))
    lastname = str(input("Surname: "))
    num = int(input("Number: "))
    postgress_insert_query = """ INSERT INTO  phone_number(name, surname, number_value) VALUES (%s,%s,%s)"""
    record_to_insert = (firstname, lastname, num)
    db_cursor.execute(postgress_insert_query, record_to_insert)
    db_connection.commit()
    print("successfully !!");
    db_connection.close()





