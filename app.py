from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        "name": "store one",
        'items': [
            {
                'name': "item1",
                "price": 15.5
            }
        ]
}
]


# We will define our api here.

# Post - the server receive data.
# Get the server has to send data.

# POST /store data: {name} creates a new store with the given name
@app.route('/store', methods=['POST'])
def create_store():
    # This is the data given when the post request was made
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> get a store for a given name
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
        return jsonify({"message": "No Store found"})


# GET /store get a list with all the stores
@app.route('/store')
def get_store_list():
    # We return a json but our stores variable is a list so we need to make a dictionary before we convert it into JSON
    return jsonify({"stores": stores})


# POST /store/<string:name>/item {name:, price} create an item in a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name, item):
    request_data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": "Store not found!"})


# GET /store/<string:name>/item get all the items in a specific store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({"message": "No Store found with that name!"})


app.run(port=5000)
