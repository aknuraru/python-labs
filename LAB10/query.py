import psycopg2
db_connection = psycopg2.connect(
	database="Phonebook",
	user='postgres',
	password='2007',
	host='localhost',
	port='5432'
)
cursor = db_connection.cursor()
db_connection.autocommit = True
choice=input("type 1 for selecting all or 2 for filter or 3 for decrease or 4 for increase")
if choice=='1':
    sql = "select * from phone_number";
elif choice=='2':
    sql = "select * from phone_number where name = \'Sasha\' ";
elif choice=='3':
    sql = "select * from phone_number  order by name desc";
elif choice=='4':
    sql = "select * from phone_number  order by name asc";
cursor.execute(sql)
info = cursor.fetchall()
print(info)