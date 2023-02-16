# importing Flask package
from flask import Flask, request, jsonify
import db_operations as db

# Creating flask application
app = Flask(__name__)

# This one is an API route for "/" url endpoint
# You can test this from browser by typing the address http://localhost:5000
@app.route('/')
def index():
    return "Hello from index"

@app.route('/greet')
def greet():
    return "Hello from greet"

#having a string variable in the request
# This is GET request (default type of request)
@app.route('/user/<username>')
def show_user(username):
  # Make the sql query to your database and e.g. search information about the user
  return 'Username: %s' % username

#Example about POST request and int variable in the request
@app.route('/post/<int:post_id>')
def show_post(post_id):
  return str(post_id)

@app.route('/search', methods=['GET'])
def search():
    args = request.args
    location = args.get('location')
    name = args.get('name')
    result = db.search(name, location)
    return jsonify(result), 200

@app.route('/insertcustomers')
def create_customers():
    db.insert_rows_to_customers()
    return "data added"


