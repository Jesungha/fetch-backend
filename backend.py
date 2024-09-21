from flask import Flask
from flask import request, jsonify, Response

from Customer import Customer

app = Flask(__name__)

'''

Call add_balance function from Customer class
Respond with 200 if successful else respond with 400

request body:
{
    "payer" : "DANNON",
    "points" : 5000,
    "timestamp" : "2020-11-02T14:00:00Z"
}

'''
@app.route('/add', methods=['POST'])

def add():
    data = request.get_json()
    return Response(status=200)

'''

Call spend_balance function from Customer class
Respond with 200 and list of payer names and number of point substracted if successful else respond with 400 and a message

request body:
{"points" : 5000}

response body:
[
    { "payer": "DANNON", "points":-100 },
    { "payer": "UNILEVER", "points":-200 },
    { "payer": "MILLER COORS", "points":-4,700 }
]

'''

@app.route('/spend', methods=['POST'])

def spend():
    data = request.get_json()
    Customer.get_customer(data['user_id']).spend(data['amount'])
    return Response(status=200)


'''

Call get_balance function from Customer class
Respond with 200 and request body and balance if successful else respond with 400

response body:
{
    "DANNON": 1000,
    ”UNILEVER” : 0,
    "MILLER COORS": 5300
}
'''

@app.route('/balance', methods=['GET'])

def balance():
    user_id = request.args.get('user_id')
    balance = Customer.get_customer(user_id).balance
    return jsonify({'balance': balance})