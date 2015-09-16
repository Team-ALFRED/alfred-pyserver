from flask import Flask, jsonify, request, send_file
app = Flask(__name__)

inv = [{"name":"Water", "quantity":10}, {"name":"Granola", "quantity":5}]
rooms = ["living room", "kitchen", "dining room"]

@app.route("/map")
def show_map():
    return send_file("static/map.png")

@app.route("/sync")
def inventory():
    return jsonify({"inv":inv,"map":rooms})

@app.route("/deliver", methods=['POST'])
def items():
    item = request.json.get('item')
    loc = request.json.get('location')

    if loc == None:
        return jsonify({"error": "Parameter 'location' is required"})

    if not(loc in rooms):
        return jsonify({"error": "Not a valid location"})

    if not(item in inv):
        return jsonify({"error": "Not a valid item"})

    # dispense item at loc
    print("Dispensing {} at {}".format(item, loc))

    inv[item] -= 1
    return jsonify({"name":item, "quantity":inv[item]})

if __name__ == "__main__":
    app.run()
