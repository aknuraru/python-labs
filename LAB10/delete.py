import psycopg2
connection = psycopg2.connect(
	database="Phonebook",
	user='postgres',
	password='2007',
	host='localhost',
	port='5432'
)
cur = connection.cursor()
connection.autocommit = True
first_old = str(input("First_old: "))
last_old = str(input("Last_old: "))
sql = f"select * from phone_number where name =\'{first_old}\' and surname = \'{last_old}\' "
cur.execute(sql)
info = cur.fetchall()
if len(info) > 0:
    sql_update = f"Delete from phone_number where  name =\'{first_old}\' and surname = \'{last_old}\'; " 
    cur.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")
connection.commit()
connection.close()