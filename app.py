from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)

my_notes = []
initial_note = {}
views = {
    "list": 0,
    "create_edit": 1
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu', methods=['GET'])
def menu():
    return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["list"])

@app.route('/create', methods=['GET'])
def create():
    return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["create_edit"])

@app.route('/edit_note/<int:note_id>', methods=['GET'])
def edit_note(note_id):
    edit_note = {}
    if len(my_notes) > 0:
        edit_note = getNote(note_id)
    else:
        return redirect(url_for('menu'))
    return render_template('content.html', my_notes = my_notes, new_note = edit_note, view=views["create_edit"])


@app.route('/submit_edit_note/<int:note_id>', methods=['POST'])
def submit_edit_note(note_id):
    prev_note = getNote(note_id)
    if request.method == 'POST':
        note_title = request.form.get('inputNoteTitle')
        note_description = request.form.get('inputNoteDescription')
        my_notes[note_id] = {
            "note_id": note_id,
            "note_title": note_title,
            "note_description": note_description,
            "note_created_date": prev_note["note_created_date"]
        }
        return render_template('content.html', my_notes = my_notes, new_note = {}, view=views["list"])

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

@app.route('/remove_note/<int:note_id>', methods=['GET'])
def remove_note(note_id):
    if len(my_notes) > 0: 
        my_notes.pop(note_id)
    return redirect(url_for('menu'))



def loadNotes(my_notes):
    my_notes = []
    return my_notes

def addNotes(note):
    my_notes.append(note)

def getNextNoteId():
    return len(my_notes)

def getNote(note_id):
    note = my_notes[note_id]
    return note

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')