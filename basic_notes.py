import datetime
# Una nota tiene un título, contenido y una fecha de creación.
# Se pueden crear, editar y eliminar notas.
# Las notas se pueden listar y buscar por título o contenido.
#
# Inicia el programa con un menú de opciones para el usuario.
# 1 Crear nota 
# 2 Ver notas ya creadas
# 3 Editar nota
# 4 Eliminar nota
# 5 Salir
#
# 1 -> Al crear una nota, se debe pedir al usuario el título y el contenido.
#       La fecha de creación se asigna automáticamente.
#       Las notas seran un objeto de una clase Nota.
#       Los atributos de la clase Nota son: título, contenido y fecha de creación.
#      Se debre crear un clase que administre las notas.
#      La clase debe tener métodos para crear, editar, eliminar y listar notas.
#      Las notas se almacenan en una lista que es un atributo de la clase que administra las notas.
#      El usuario al crear el tituto el prgrama debe verificar que no exista una nota con el mismo título.
#      El título debe ser único, si el usuario intenta crear una nota con un título que ya existe,
#      se le debe informar y pedir un título diferente.
#      Se debe confirmar que la nota ha sido creada y mostrar la nota creada.
#      No se permiten títulos vacíos.
# 2 -> Al ver las notas, se deben listar todas las notas con su título y fecha de creación.
# 3 -> Al editar una nota, se debe pedir al usuario el título de la nota a editar.
#      Al elegir la nota se debe preguntar al suario si quiere cambiar el título, el contenido o ambos.
#      Si el usuario elige cambiar el título, se debe pedir el nuevo título.
#      Si el usuario elige cambiar el contenido, se debe pedir el nuevo contenido.
#      Se debe confirmar que la nota ha sido editada y mostrar la nota editada.
#  4 -> Al eliminar una nota, se debe pedir al usuario el título de la nota a eliminar.
#       Si el titulo de la nota exista, se debe preguntar al usuario si está seguro de que quiere eliminar la nota.
#       Al confirmar, se debe eliminar la nota y confirmar que la nota ha sido eliminada.
#   5 -> Salir del programa.
#

print("Welcome to the Notes App")


class Note:
    def __init__(self, title, content, datetime): # Note constructor
        self.title = title
        self.content = content
        self.datetime = datetime

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content): # Create note method
        note = Note(title, content, datetime.datetime.now()) 
        self.notes.append(note) # Append note to notes list

    def view_notes(self): # View notes method
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(f"Title: {note.title}\nCreated on: {note.datetime}\nContent: {note.content}")
    
    def edit_note(self):
        if not self.notes: # Check if there are notes to edit
            print("No notes available to edit.")
            return
        for i, note in enumerate(self.notes): # List notes with index
            print(f"{i + 1}. {note.title}")
        try: # Try to get valid input from user
            choice = int(input("Select the number of the note to edit: ")) - 1 # Adjust for 0-based index
            choice_note = self.notes[choice]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
        
        def get_yes_no_input(prompt):
            '''Helper function to get a yes/no response from the user.'''
            while True:
                response = input(prompt).lower().strip()
                if response in ['yes', 'y']:
                    return True
                elif response in ['no', 'n']:
                    return False
                else:
                    print("Please enter 'yes' or 'no'.")

        if get_yes_no_input("Do you want to change the title? (yes/no): "): # Ask if user wants to change title
            while True:
                new_title = input("Enter the new title: ").strip()
                if new_title:
                    choice_note.title = new_title
                    break
                else: # If title is empty, ask again
                    print("Title cannot be empty. Please enter a valid title.")
        # Ask if user wants to change content        
        if get_yes_no_input("Do you want to change the content? (yes/no): "):
            new_content = input("Enter the new content: ").strip()
            choice_note.content = new_content
        
        print("Note updated successfully.") # Confirm note update
        print(f"Title: {choice_note.title}\nCreated on: {choice_note.datetime}\nContent: {choice_note.content}")

    def delete_note(self):
        pass
manager = NoteManager()

while True:
    print("\nMenu:")
    print("1. Create Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

    option = input("Choose an option (1-5): ")
    if option == '1':
        title_note = input("Enter note title: ").strip()
        content_note = input("Enter note content: ").strip()
        manager.create_note(title_note, content_note)
    elif option == '2':
        manager.view_notes()
    elif option == '3':
        manager.edit_note()
    elif option == '4':
        manager.delete_note()
    elif option == '5':
        print('Exiting the program.')
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")


