from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import add_item, get_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', items=get_items(), route='display')

@app.route('/add', methods = ["GET","POST"])
def add():
    if (request.method== "GET" ):
        return render_template('add.html')
    else:
        title = request.form.get('taskname')
        add_item(title)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True)