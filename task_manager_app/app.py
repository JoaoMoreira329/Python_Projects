from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Flask -> is a micro web framework for creating web applications in Python.
# render_template -> is used for rendering HTML templates.
# request -> is used to access the data sent with the HTTP request.
# redirect and url_for -> are used for URL redirection.
# Flask-SQLAlchemy is an extension for Flask that simplifies working with databases.

#  CREATE A FLASK APP AND CONFIGURE THE DATABASE

app = Flask(__name__)   #An instance of the Flask application is created
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'    #The database is configured using SQLite, and the database file will be named 'tasks.db'
db = SQLAlchemy(app)    #An instance of SQLAlchemy is created and initialized with the Flask app, enabling interaction with the database.


#   CREATE THE DB MODEL

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)  
    description = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# SETTING THE ROUTES


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form.get('name')
    description = request.form.get('description')
    new_task = Task(name=name, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update_task/<int:id>')
def update_task(id):
    task = Task.query.get(id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        
        db.create_all()  
    app.run(debug=True)