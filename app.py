from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/<name>")
def greet(name):
    return "Hello " + name.upper()

if __name__=="__main__":
    app.run(debug=True)

