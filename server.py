from flask import Flask, jsonify, request
app = Flask(__name__)

inv = {"Water": 10, "Granola": 5}
map = {"living room": "foo", "kitchen": "bar", "dining room": "bingo"}

@app.route("/assets/map")
def show_map():
    return "display the map"

@app.route("/sync")
def inventory():
    return jsonify({"inv":inv,"map":map})

@app.route("/items/<string:item>", methods=['POST'])
def items(item):
    loc = request.form.get('location', type=str)

    if loc == None:
        return jsonify({"error": "Parameter 'location' is required"})

    if not(loc in map):
        return jsonify({"error": "Not a valid location"})

    # dispense item at loc

    if not(item in inv):
        return jsonify({"error": "Not a valid item"})

    inv[item] -= 1
    return jsonify({"name":item, "count":inv[item]})

if __name__ == "__main__":
    app.run()
