from flask import Flask, render_template
import json
app = Flask(__name__)

my_notes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes')
def notes():
    return render_template('index.html', my_notes = True)

@app.route('/start')
def start():
    a = '{ "name":"John", "age":30, "city":"New York"}'
    addNotes(json.loads(a))
    return render_template('start.html')

def loadNotes(my_notes):
    my_notes = []
    return my_notes

def addNotes(note):
    my_notes.append(note)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')