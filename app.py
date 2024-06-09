from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)

datas = [
    {
        "id": 1,
        "title": "Test Todo 1"
    },
    {
        "id": 2,
        "title": "Test Todo 2"
    },
    {
        "id": 3,
        "title": "Test Todo 3"
    },
    {
        "id": 4,
        "title": "Test Todo 4"
    },
    {
        "id": 5,
        "title": "Test Todo 5"
    }
]

@app.route("/home", methods = ["GET", "POST"])
@app.route("/")
def home():
    if request.method == "POST":
        title = request.form["title"]
        print("Title: ", title)
        new_todo = {
            "id": datas.__len__()+1,
            "title": title
        }
        datas.append(new_todo)
        
    return render_template('index.html', data=datas)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
