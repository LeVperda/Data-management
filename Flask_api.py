from flask import Flask, request, jsonify
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="*******",
    database="mybusiness"
)

cursor = mydb.cursor()

app = Flask(__name__)

# 1
# a. Return all customers

@app.route('/customers', methods=['GET'])
def get_customers():
    cursor.execute("SELECT cust_name FROM customer")
    result = cursor.fetchall()
    
    return jsonify(result), 200

# b. Specific customer

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_id(customer_id):
    query = ("SELECT cust_name FROM customer WHERE customer_id = %s")
    cursor.execute(query, (customer_id,))
    result = cursor.fetchall()

    return jsonify(result), 200

# c. Add a customer

@app.route('/customers/add', methods=['POST'])
def add_customer(customer_data):
    query = "INSERT INTO customer (cust_name, city, grade, salesman_id) VALUES (%s, %s, %s, %s)"
    values = (customer_data['name'], customer_data['city'], customer_data['grade'], customer_data['salesman_id'])
    cursor.execute(query, values)
    mydb.commit()

# d. Replace customer by id

@app.route('/customer/update/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id, customer_data):
    query = "UPDATE customer SET cust_name = %s, city = %s, grade = %s, salesman_id = %s WHERE customer_id = %s"
    values = (customer_data['name'], customer_data['city'], customer_data['grade'], customer_data['salesman_id'], customer_id)
    cursor.execute(query, values)
    mydb.commit()

# e. Delete customer

@app.route('customer/delete/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    query = "DELETE FROM customer WHERE customer_id = %s"
    cursor.execute(query, (customer_id,))
    mydb.commit()

# 2. Same API for salesman
# a.

@app.route('/salesman', methods=['GET'])
def get_salesman():
    cursor.execute("SELECT name FROM salesman")
    result = cursor.fetchall()
    
    return jsonify(result), 200

# b.

@app.route('/salesman/<int:salesman_id>', methods=['GET'])
def get_salesman_id(salesman_id):
    query = ("SELECT name FROM salesman WHERE salesman_id = %s")
    cursor.execute(query, (salesman_id,))
    result = cursor.fetchall()

    return jsonify(result), 200

# c.

@app.route('/salesman/add', methods=['POST'])
def add_salesman(salesman_data):
    query = "INSERT INTO salesman (name, city, comission) VALUES (%s, %s, %s)"
    values = (salesman_data['name'], salesman_data['city'], salesman_data['comission'])
    cursor.execute(query, values)
    mydb.commit()

# d.

@app.route('/salesman/update/<int:salesman_id>', methods=['PUT'])
def update_salesman(salesman_id, salesman_data):
    query = "UPDATE salesman SET name = %s, city = %s, comission = %s WHERE salesman_id = %s"
    values = (salesman_data['name'], salesman_data['city'], salesman_data['comission'], salesman_id)
    cursor.execute(query, values)
    mydb.commit()

# e.

@app.route('salesman/delete/<int:salesman_id>', methods=['DELETE'])
def delete_salesman(salesman_id):
    query = "DELETE FROM salesman WHERE salesman_id = %s"
    cursor.execute(query, (salesman_id,))
    mydb.commit()


if __name__ == '__main__':
    app.run(debug=True)