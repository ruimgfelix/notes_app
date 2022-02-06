from flask import Flask, render_template, request, redirect, url_for
import datetime
app = Flask(__name__)

my_notes = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', my_notes = my_notes)

@app.route('/submit_note', methods=['POST'])
def submit_note():
    today = datetime.datetime.now()
    if request.method == 'POST':
        note_title = request.form.get('inputNoteTitle')
        note_description = request.form.get('inputNoteDescription')
        new_note = {
            "note_title": note_title,
            "note_description": note_description,
            "note_created_date": today.strftime("%d %B %Y, %H:%M:%S")
        }
        addNotes(new_note)
        return redirect(url_for('menu'))

def loadNotes(my_notes):
    my_notes = []
    return my_notes

def addNotes(note):
    my_notes.append(note)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')