import datetime

print("Welcome to the Notes App")

# Note class to represent a single note
class Note: 
    def __init__(self, title, content, datetime): # Note constructor
        self.title = title
        self.content = content
        self.datetime = datetime

# NoteManager class to handle note operations            
class NoteManager:
    def __init__(self):
        self.notes = []
    @staticmethod
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

    def create_note(self, title, content): # Create note method
        note = Note(title, content, datetime.datetime.now()) 
        self.notes.append(note) # Append note to notes list

    def view_notes(self): # View notes method
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(f"Title: {note.title}\nCreated on: {note.datetime}\nContent: {note.content}")
    
    def edit_note(self): # Edit note method
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
        # Ask if user wants to change title
        if self.get_yes_no_input("Do you want to change the title? (yes/no): "): 
            while True:
                new_title = input("Enter the new title: ").strip()
                if new_title:
                    choice_note.title = new_title
                    break
                else: # If title is empty, ask again
                    print("Title cannot be empty. Please enter a valid title.")
        # Ask if user wants to change content        
        if self.get_yes_no_input("Do you want to change the content? (yes/no): "):
            new_content = input("Enter the new content: ").strip()
            choice_note.content = new_content
        
        print("Note updated successfully.") # Confirm note update
        print(f"Title: {choice_note.title}\nCreated on: {choice_note.datetime}\nContent: {choice_note.content}")

    def delete_note(self): # Delete note method
        if not self.notes: # Check if there are notes to delete
            print("No notes available to delete.")
            return
        for i, note in enumerate(self.notes): # List notes with index
            print(f"{i + 1}. {note.title}")
        try: # Try to get valid input from user
            choice = int(input("Select the number of the note to delete: ")) - 1 # Adjust for 0-based index
            choice_note = self.notes[choice]
        except (ValueError, IndexError):
            print("Invalid selection.")
            return
        if self.get_yes_no_input("Are you sure you want to delete this note? (yes/no): "): # Confirm deletion
            self.notes.remove(choice_note)
            print("Note deleted successfully.")
        else:
            print("Deletion cancelled.")


manager = NoteManager() # Create an instance of NoteManager

# Main loop for user interaction
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


