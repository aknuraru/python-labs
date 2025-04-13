import psycopg2
db_connection=psycopg2.connect(
    database="Phonebook",
	user='postgres',
	password='2007',
	host='localhost',
	port= '5432'
)
db_cursor=db_connection.cursor()
db_connection.autocommit=True
#look   for firts & last name
first_old = str(input("First_old: "))
last_old = str(input("Last_old: "))
num_old = int(input("Num_old: "))
sql_look = f"select * from phone_number where name =\'{first_old}\' and surname = \'{last_old}\' and number_value = \'{num_old}\' "
db_cursor.execute(sql_look)
info = db_cursor.fetchall()
if len(info) > 0:
    new_first = str(input("First_new: "))
    new_last = str(input("Last_new: "))
    new_phone = int(input("Num_new: "))
    sql_update = f"Update phone_number set number_value =\'{new_phone}\', name =\'{new_first}\', surname =\'{new_last}\' where name =\'{first_old}\' and surname = \'{last_old}\'; " 
    db_cursor.execute(sql_update)
    print("successfully !!");
else:
    print("this people name is not in phonebook")
db_connection.commit()
db_connection.close()