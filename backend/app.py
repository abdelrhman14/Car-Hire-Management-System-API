from flask import Flask
import psycopg2
from flask import jsonify, request
from http import HTTPStatus



app = Flask(__name__)
conn = psycopg2.connect(database="backend_system", user="postgres", password="246800", host="localhost", port="5432")

# Connect to the database

# Retrieve All Customers
@app.route('/retrieve_all_customer/', methods=[ "GET"],endpoint='func1')
def retrieve_all_customer():
    if request.method == "GET":
        cur = conn.cursor()
        cur.execute(
                f"""SELECT "Customer_Id", "First_Name", "Last_Name","Email" ,"Phone", "Address" FROM Customer; """
                )
        results = cur.fetchall()
        if results:
            return jsonify(results)
        else:
            cur.close()
            response_body = {
                        "message": "No customers were found.",
                    }
            response = jsonify(response_body)
            response.status_code = HTTPStatus.NOT_FOUND
            return response

@app.route('/customer/<int:customer_id>/', methods=[ "GET"],endpoint='func2')
def get_customer(customer_id):
    if request.method == "GET":
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM Customer WHERE "Customer_Id" = {customer_id}; """)
        results = cur.fetchall()
        if results:
            cur.close()
            return jsonify(results)
        else:
            cur.close()
            response_body = {
                        "message": "No customers were found.",
                    }
            response = jsonify(response_body)
            response.status_code = HTTPStatus.NOT_FOUND
            return response
        

@app.route('/del_customer/<int:customer_id>/', methods=[ "POST"],endpoint='func3')
def del_customer(customer_id):
    if request.method == "POST":
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM Customer WHERE "Customer_Id" = {customer_id}; """)
        results = cur.fetchall()
        if results:
            cur.execute(f"""DELETE FROM Customer WHERE "Customer_Id" = {customer_id }; """)
            conn.commit()
            cur.close()
            response_body = {
                        "message": "Deleted Successfuly.",
                    }
            response = jsonify(response_body)
            return response
        else:
            cur.close()
            response_body = {
                         "message": f"Customer with id: {customer_id} was not found.",
                    }
            response = jsonify(response_body)
            response.status_code = HTTPStatus.NOT_FOUND
            return response

@app.route('/add_customer/', methods=["GET", "POST"],endpoint='func4')
def add_customer():
    if request.method == "POST":
        Customer_Id = int(request.form['Customer_Id'])
        First_Name = request.form['First_Name']
        Last_Name = request.form['Last_Name']
        Email = request.form['Email']
        Phone = request.form['Phone']
        Address = request.form['Address']

        cur = conn.cursor()
        # Insert data into the table

        cur.execute('INSERT INTO customer ("Customer_Id","First_Name", "Last_Name", "Email", "Phone", "Address")'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            (Customer_Id,First_Name,Last_Name,Email,Phone ,Address))

        conn.commit()
        cur.close()
        response_body = {
                        "message": "Successfuly.",
                    }
        response = jsonify(response_body)
        return response
       
@app.route('/update_customer/<int:customer_id>', methods=["GET", "POST"],endpoint='func5')
def update_customer(customer_id):
    if request.method == "POST":
        cur = conn.cursor()
        cur.execute(f"""SELECT * FROM Customer WHERE "Customer_Id" = {customer_id}; """)
        results = cur.fetchall()
        if results:
            Customer_Id = customer_id
            First_Name = request.form['First_Name']
            Last_Name = request.form['Last_Name']
            Email = request.form['Email']
            Phone = request.form['Phone']
            Address = request.form['Address']
            cur.execute(f"""UPDATE customer SET "First_Name" = {First_Name}, "Last_Name"={Last_Name},"Email"={Email}, "Phone"={Phone}, "Address" = {Address} WHERE "Customer_Id"= {Customer_Id}; """)
            conn.commit()
            cur.close()
            response_body = {
                        "message": "UPDATE Successfuly.",
                    }
            response = jsonify(response_body)
            return response
        else:
            cur.close()
            response_body = {
                        "message": "No customers were found.",
                    }
            response = jsonify(response_body)
            response.status_code = HTTPStatus.NOT_FOUND
            return response

 
