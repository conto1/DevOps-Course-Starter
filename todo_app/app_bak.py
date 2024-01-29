from flask import Flask, render_template, request, redirect, url_for
#from todo_app.data.session_items import add_item, get_items
#from todo_app.flask_config import Config


#app.config.from_object(Config())
app = Flask(__name__, template_folder="templates")

#todos = [{"task": "Sample Todo", "done": False}]
todos = [{"task": "Sample Todo", "done": False}]
@app.route('/')
def index():
    #return 'Hello World!'
    items = get_items()
    return render_template('index.html', todos = todos)

@app.route('/add', methods = ["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))


@app.route('/edit/<int:index>', methods=['GET','POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[[index]]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_todo(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)