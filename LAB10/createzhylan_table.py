import psycopg2
connection = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='2007',
	host='localhost',
	port= '5432'
)
connection.autocommit = True
cur = connection.cursor()
sql_table = '''CREATE TABLE Snakedata(
   user_login VARCHAR(255) NOT NULL,
   last_score INT,
   last_level INT,
   last_FPS INT,
   snake_len INT,
   wall_len INT,
   snake_x INT,
   snake_y INT,
   record INT
);'''
cur.execute(sql_table)
print("Database,table has been created successfully(xoxo) !!");
connection.close()