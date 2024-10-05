#Calculate grade end
def get_students():
    liste_note = []
    note1 = int(input("Enter the student's 1rd grade"))
    liste_note.append(note1)
    note2 = int(input("Enter the student's 1rd grade"))
    liste_note.append(note2)
    note3 = int(input("Enter the student's 3rd grade"))
    liste_note.append(note3)
    return  liste_note
def  view_note(liste_note):
    for note in liste_note:
        print (f"Note : {note}")
def  get_average(list_note):
    suma = 0
    average = 0
    for note in list_note:
        suma += note
    average = suma/3
    return average
note_end = get_students()
view = view_note(note_end)
average_end = get_average(note_end)
print (f"la nota final es  : {average_end}")