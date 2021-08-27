from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "id": 1,
        "name": "Sohan Patil",
        "contact": "8108945567",
        "done": False,
    },
    {
        "id": 2,
        "name": "Vikas Patil",
        "contact": "9619552583",
        "done": False,
    }
]

@app.route("/")
def hello():
    return "Hello, Welcome to Sohan's Creations"

@app.route("/add-data", methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data",
        }, 400)
    
    contact = {
        "id": contacts[-1]["id"] + 1,
        "name": request.json['name'],
        "contact": request.json.get('contact'),
        "done": False
    }
    contacts.append(contact)

    return jsonify({
        "status": "success",
        "message": "Contact added sucessfully"
    })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": contacts
    })

if __name__ == "__main__":
    app.run(debug = True)    