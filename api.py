from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '010899572020'
app.config['MYSQL_DB'] = 'classicmodels'

mysql =MySQL(app)

@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM classicmodels.customers')
        customers = cur.fetchall()
        cur.close()
        return jsonify(customers)
    except Exception as e:
        print(f'Error retrieve: {e}')
        return jsonify([]), 500
    
@app.route('/api/customers', methods=['POST'])
def create_customers():
    try:
        data = request.json
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO customers (age) VALUES (%s)', (data['age']))
        mysql.connection.commit()
        customerNumber = cur.lastrowid
        cur.closeid
        return jsonify({'id': customerNumber, age: data['age']}), 201
    except Exception as e:
        print(f'Error create customers: {e}')
        return jsonify({'Failed to create'})

@app.route('/api/customers', method=['DELETE'])
def delete_customers():
    try:
        cur=mysql.connection.cursor()
        cur.execute('DELETE FROM customers WHERE id=%s', (customerNumber))
        mysql.connection.commit()
        cur.close()
        return jsonify({'CustomerNumber delete'})
    except Exception as e:
        print(f'Error delete: {e}')
        return jsonify({'Failed to delete'})
    
@app.route('/api/customers/<VARCHAR:state', method=['PUT'])
def update_customers():
    try:
        data = request.json
        cur = mysql.connection.cursor()
        cur.execute('UPDATE customers SET state = %s, state')
        mysql.connection.commit()
        cur.close()
        return jsonify({'state: state'})
    except Exception as e:
        print(f'Error update')
        return jsonify({'Failed to Update'})

if __name__ == '__main__':
    app.run()    


