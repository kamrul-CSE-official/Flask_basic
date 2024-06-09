from flask import Flask, render_template  # type: ignore


app = Flask(__name__)


datas =  {
    "name": "MD.Kamrul Hasan",
    "numbers": [1,2,3,4,5,6,7,8,9,10]
}

@app.route("/home")
@app.route("/")
def home():
    return render_template('index.html', data=datas)

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": 
    app.run(debug=True)