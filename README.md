# 📝 Basic Notes App

A simple command-line notes manager built in Python.  
This project was created to practice object-oriented programming (OOP) concepts such as classes, methods, and basic data management.

## Features

- Create notes with a title, content, and timestamp  
- View all saved notes in a clean format  
- Edit the title or content of existing notes  
- Delete notes with confirmation prompts  
- User-friendly input validation  

## How It Works

When you start the program, you'll see a menu with options:  

    1. Create Note

    2. View Notes

    3. Edit Note

    4. Delete Note

    5. Exit

Notes are stored in memory during the session. Each note has:  

- **Title** → Short text describing the note  
- **Content** → The body of the note  
- **Created on** → A timestamp when the note was added  

## Example

        Welcome to the Notes App

        Menu:

        1. Create Note

        2. View Notes

        3. Edit Note

        4. Delete Note

        5 Exit


        Choose an option (1-5): 1
        Enter note title: Shopping List
        Enter note content: Eggs, Milk, Bread
        Note created successfully.

## Requirements

- Python 3.7+  
- No external libraries required  

## How to Run

1. Clone this repository  
2. Run the script in your terminal:  

        python basic_notes.py

Future Improvements

- Save notes to a file (JSON or text)

- Load notes when restarting the program

- Add search functionality

- Add categories or tags

This project is a learning exercise. Feel free to use it, modify it, and expand it as you learn more about Python.
