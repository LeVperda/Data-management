from flask import Flask, request, jsonify
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Nikitos99_09",
    database="mybusiness"
)

app = Flask(__name__)

@app.route('/customers', methods=['GET'])
def get_customers():
    cursor = mydb.cursor()
    query = "SELECT * FROM customer"
    
    city = request.args.get('city')
    grade = request.args.get('grade')
    salesman_id = request.args.get('salesman_id')
    
    if city:
        query += " WHERE city = '%s'" % city
    
    if grade:
        if 'WHERE' not in query:
            query += " WHERE grade = %s" % grade
        else:
            query += " AND grade = %s" % grade
    
    if salesman_id:
        if 'WHERE' not in query:
            query += " WHERE salesman_id = %s" % salesman_id
        else:
            query += " AND salesman_id = %s" % salesman_id
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    customers = []
    for row in rows:
        customer = {
            'id': row[0],
            'name': row[1],
            'city': row[2],
            'grade': row[3],
            'salesman_id': row[4]
        }
        customers.append(customer)
    
    return jsonify(customers)


if __name__ == '__main__':
    app.run(debug=True)