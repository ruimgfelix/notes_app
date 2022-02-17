from flask import Flask, render_template, request, redirect, url_for
import datetime
import time
app = Flask(__name__)

my_notes = []
initial_note = {}
views = {
    "list": 0,
    "create_edit": 1
}
search_flag = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu', methods=['GET'])
def menu():
    return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["list"], search_flag = False)

@app.route('/create', methods=['GET'])
def create():
    return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["create_edit"], search_flag = False)

@app.route('/edit_note/<int:note_id>', methods=['GET'])
def edit_note(note_id):
    edit_note = {}
    if len(my_notes) > 0:
        index = get_index(note_id)

        edit_note = my_notes[index]
    else:
        return redirect(url_for('menu'))
    return render_template('content.html', my_notes = my_notes, new_note = edit_note, view=views["create_edit"], search_flag = False)


@app.route('/submit_edit_note/<int:note_id>', methods=['POST'])
def submit_edit_note(note_id):
    index = get_index(note_id)
    prev_note = my_notes[index]
    if request.method == 'POST':
        note_title = request.form.get('inputNoteTitle')
        note_description = request.form.get('inputNoteDescription')
        my_notes[index] = {
            "note_id": note_id,
            "note_title": note_title,
            "note_description": note_description,
            "note_created_date": prev_note["note_created_date"]
        }
        return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["list"], search_flag = False)

@app.route('/submit_note', methods=['POST'])
def submit_note():
    today = datetime.datetime.now()
    if request.method == 'POST':
        note_title = request.form.get('inputNoteTitle')
        note_description = request.form.get('inputNoteDescription')
        new_note = {
            "note_id": getNextNoteId(),
            "note_title": note_title,
            "note_description": note_description,
            "note_created_date": today.strftime("%d %B %Y, %H:%M:%S")
        }
        addNotes(new_note)
        return redirect(url_for('menu'))

@app.route('/filter', methods=['POST'])
def search():
    if request.method == 'POST':
        filter_search = request.form.get('filter_notes')
        search_notes = []
        if (filter_search != ""):
            search_notes = filter_notes(my_notes, filter_search)
        
        return render_template('content.html', my_notes = search_notes, new_note = {}, view=views["list"], search_flag = True)

@app.route('/order/<string:method>', methods=['POST'])
def order_notes(method):
    if request.method == 'POST':
        order_notes_by_method(method)
        return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["list"], search_flag = False)

@app.route('/remove_note/<int:note_id>', methods=['GET'])
def remove_note(note_id):
    my_notes.pop(get_index(note_id))
    return redirect(url_for('menu'))


def order_notes_by_method(method):
    if method == "title":
        my_notes.sort(key=lambda x: x["note_title"])
    elif method == "type":
        my_notes.sort(key=lambda x: x["type"])
    elif method == "oldest":
        my_notes.sort(key=lambda x: datetime.datetime.strptime(x["note_created_date"], '%d %B %Y, %H:%M:%S'))
    else:
        my_notes.sort(key=lambda x: datetime.datetime.strptime(x["note_created_date"], '%d %B %Y, %H:%M:%S'), reverse=True)
    

def filter_notes(notes, string_search):
    result_notes = list(filter(lambda ite: string_search in ite["note_title"] or string_search in ite["note_description"], notes))
    return result_notes

def loadNotes(my_notes):
    my_notes = []
    return my_notes

def addNotes(note):
    my_notes.append(note)

def getNextNoteId():
    return len(my_notes)

def get_index(note_id):
    index = 0
    if len(my_notes) > 0:
        for i in range(len(my_notes)):
            elem = my_notes[i]["note_id"]
            if elem == note_id:
                index = i
    return index




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')