from flask import Flask
from flask import request, jsonify, Response

from Customer import Customer

app = Flask(__name__)
first_customer = Customer(1, "test")
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
    try:
        data = request.get_json()
        first_customer.add_balance(data['payer'], data['points'], data['timestamp'])
        return Response(status=200)
    except Exception as e:
        return jsonify({"error": "insufficient balance"}), 400
    

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
    try:
        data = request.get_json()
        return jsonify(first_customer.spend_balance(data['points']))
    except:
        return jsonify({"error": "insufficient balance"}), 400


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
    try:
        return jsonify(first_customer.get_balance())
    except:
        return jsonify({"error": "error"}), 400
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)# run the app on port 5000 change if needed