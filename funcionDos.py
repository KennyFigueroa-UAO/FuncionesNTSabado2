#crear una funcion que de manera aleatoria crea una lista de n notas entrears y deveulve esa lista
import random

def createNotes(notesQ):
    notes = []

    for _ in range(notesQ):
        note = round(random.uniform(1,5),1)
        notes.append(note)

    return notes

notes = createNotes(10)
print(notes)