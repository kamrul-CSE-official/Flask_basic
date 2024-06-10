from flask import Flask, render_template, request, redirect

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

@app.route("/home", methods=["GET", "POST"])
@app.route("/")
def home():
    if request.method == "POST":
        title = request.form.get("title")
        if title:  # Check if title is not empty
            new_id = max(todo["id"] for todo in datas) + 1 if datas else 1  # Ensure unique ID
            new_todo = {
                "id": new_id,
                "title": title
            }
            datas.append(new_todo)
    return render_template('index.html', data=datas)

@app.route("/remove/<int:todoid>")
def removeTodo(todoid):
    todo_to_remove = next((todo for todo in datas if todo["id"] == todoid), None)
    if todo_to_remove:
        datas.remove(todo_to_remove)
    return redirect('/')


@app.route("/update/<int:todoid>", methods=['GET'])
def updateTodo(todoid):
    for todo in datas:
        if todo['id'] == todoid:
            return render_template('update.html', todo=todo)
    return redirect("/")


@app.route("/updateTodo", methods=['POST'])
def update():
    title = request.form['title']
    id = int(request.form['id'])  # Convert id to int for comparison
    for todo in datas:
        if todo['id'] == id:
            todo['title'] = title
            return redirect('/')
    return redirect('/')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
