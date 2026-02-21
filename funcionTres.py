#Crear una funcion que reciba una lista de numeros enteros y calcules su promedio para retornarlo
import random

def createAverage(notes):
    # total = 0

    # for note in notes:
        # total += note
    # for i in range(len(notes)):
    #     total += notes[i]
    return sum(notes) / len(notes)

def createNotes(notesQ):
    notes = []
    for _ in range(notesQ):
        note = round(random.uniform(1,5),1)
        notes.append(note)
    return notes

notes = createNotes(5)
print(notes)

average = createAverage(notes)
print(average)