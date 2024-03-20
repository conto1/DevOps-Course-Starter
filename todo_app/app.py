import os
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data import trello_items

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
        return render_template('index.html', items=trello_items.get_items(), route='display')

@app.route('/add', methods = ["GET","POST"])
def add():
    if (request.method== "GET"):
        return render_template('index.html',statuses=trello_items.get_lists())
    else:
        item = {}
        item['name'] = request.form.get('taskname')
        item['idList'] = os.getenv("TRELLO_TODO_LIST_ID")
        trello_items.add_item(item)
        return redirect('/')
    
@app.route('/delete')
def deletetodo():
    id = request.values.get("id","")
    trello_items.delete_item(id)
    return redirect('/')  

@app.route('/complete')
def complete_item():
    id = request.values.get("id","")
    trello_items.complete_item(id)
    return redirect('/')
    
@app.route('/start')
def start_item():
    id = request.values.get("id","")
    trello_items.start_item(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)