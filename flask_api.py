from flask import Flask,jsonify

app = Flask(__name__)

db = {"name1":"name"}

@app.route("/")
def index():
    return "Hello"

@app.route("/database")
def database():
    return jsonify(db)

if __name__ == "__main__":
    app.run(debug = True)