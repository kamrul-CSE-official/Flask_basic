from flask import Flask 

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return "Bismillah"

@app.route("/about")
def about():
    return "This is about"


if __name__ == "__main__": 
    app.run()