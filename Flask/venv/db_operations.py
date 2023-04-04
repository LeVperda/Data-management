import mysql.connector as mysql
mydb = mysql.connect(
  host="localhost",
  port="3310",
  user="test",
  password="test",
  database="test"
)
mycursor = mydb.cursor()

def create_table():
  mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
  print("Table created")

def insert_data():
  sql ="INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = ("John","Highway 21")
  mycursor.execute(
    sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

def insert_rows_to_customers():
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
  ]

  mycursor.executemany(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "was inserted.")


def search(name, address):
  condition = ""
  if None not in (name, address):
    condition = f"where name='{name}' and address='{address}'"
  elif name is not None:
    condition = f"where name='{name}'"
  elif address is not None:
    condition = f"where address='{address}'"
  sql = f"SELECT * from customers {condition}"
  print(sql)

  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  return create_dict(myresult)


def editCustomer(id, customer):
  sql = f"UPDATE customers SET name= '{customer['name']}', address='{customer['address']}' WHERE id = '{id}'"
  mycursor.execute(sql)
  mydb.commit()

def create_dict(myresult):
  dict_data = []
  # get the column names as a tuple
  column_names = mycursor.column_names
  for r in myresult:
    row_zip = zip(column_names, r)
    row_dict = dict(row_zip)
    dict_data.append(row_dict)
  return dict_data



