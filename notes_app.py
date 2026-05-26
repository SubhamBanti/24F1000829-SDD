def add_note():
    note = input("Enter your note: ")
    with open("my_notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("my_notes.txt", "r") as file:
            notes = file.readlines()
            print("\n--- Your Saved Notes ---")
            if not notes:
                print("No notes found yet.")
            else:
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found yet.")
def edit_note():
    try:
        with open("my_notes.txt", "r") as file:
            notes = file.readlines()
        if not notes:
            print("No notes to edit.")
            return
        print("\n--- Your Saved Notes ---")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note.strip()}")
        try:
            num = int(input("Enter the note number to edit: "))
            if 1 <= num <= len(notes):
                new_note = input("Enter the new content: ")
                notes[num-1] = new_note + "\n"
                with open("my_notes.txt", "w") as file:
                    file.writelines(notes)
                print("Note updated!")
            else:
                print("Invalid note number.")
        except ValueError:
            print("Please enter a valid number.")
    except FileNotFoundError:
        print("No notes found yet.")

def search_notes():
    keyword = input("Enter keyword to search: ").strip()
    found = False
    try:
        with open("my_notes.txt", "r") as file:
            print(f"\n--- Notes containing '{keyword}' ---")
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True
        if not found:
            print("No matching notes found.")
    except FileNotFoundError:
        print("No notes found yet.")

# Simple menu loop
while True:
    print("\n1. Add Note\n2. View Notes\n3. Search Notes\n4. Edit Note\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        search_notes()
    elif choice == '4':
        edit_note()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
