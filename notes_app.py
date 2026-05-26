import json
import os
from datetime import datetime

DATA_FILE = "notes.json"


def load_notes():
    if not os.path.exists(DATA_FILE):
        return {"next_id": 1, "notes": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_notes(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_note():
    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("Title cannot be empty.")
    content = input("Content: ").strip()
    data = load_notes()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": data["next_id"],
        "title": title,
        "content": content,
        "created_at": now,
        "updated_at": now,
        "reminder_at": None,
    }
    data["notes"].append(note)
    data["next_id"] += 1
    save_notes(data)
    print(f"Note #{note['id']} saved!")


def view_all_notes():
    data = load_notes()
    if not data["notes"]:
        print("No notes found.")
        return
    print()
    for note in data["notes"]:
        reminder = " [R]" if note.get("reminder_at") else ""
        print(f"  [{note['id']}] {note['title']}{reminder} ({note['created_at'][:10]})")


def view_note_detail():
    data = load_notes()
    try:
        nid = int(input("Enter note ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    note = next((n for n in data["notes"] if n["id"] == nid), None)
    if not note:
        print("Note not found.")
        return
    print(f"\n--- Note #{note['id']} ---")
    print(f"Title:      {note['title']}")
    print(f"Content:    {note['content']}")
    print(f"Created:    {note['created_at']}")
    print(f"Updated:    {note['updated_at']}")
    if note.get("reminder_at"):
        print(f"Reminder:   {note['reminder_at']}")
    else:
        print("Reminder:   (none)")


def edit_note():
    data = load_notes()
    try:
        nid = int(input("Enter note ID to edit: "))
    except ValueError:
        print("Invalid ID.")
        return
    note = next((n for n in data["notes"] if n["id"] == nid), None)
    if not note:
        print("Note not found.")
        return
    print(f"Current title: {note['title']}")
    new_title = input("New title (leave empty to keep): ").strip()
    if new_title:
        note["title"] = new_title
    print(f"Current content: {note['content']}")
    new_content = input("New content (leave empty to keep): ").strip()
    if new_content:
        note["content"] = new_content
    if new_title or new_content:
        note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_notes(data)
        print("Note updated!")
    else:
        print("No changes made.")


def delete_note():
    data = load_notes()
    try:
        nid = int(input("Enter note ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    note = next((n for n in data["notes"] if n["id"] == nid), None)
    if not note:
        print("Note not found.")
        return
    print(f"Note: [{note['id']}] {note['title']}")
    confirm = input("Are you sure you want to delete this note? (y/n): ").strip().lower()
    if confirm == "y":
        data["notes"] = [n for n in data["notes"] if n["id"] != nid]
        save_notes(data)
        print("Note deleted.")
    else:
        print("Deletion cancelled.")


def search_notes():
    data = load_notes()
    if not data["notes"]:
        print("No notes found yet.")
        return
    while True:
        keyword = input("Enter keyword to search: ").strip()
        if keyword:
            break
        print("Keyword cannot be empty.")
    keyword_lower = keyword.lower()
    matches = []
    for note in data["notes"]:
        if keyword_lower in note["title"].lower() or keyword_lower in note["content"].lower():
            matches.append(note)
    if not matches:
        print("No matching notes found.")
        return
    print(f"\n--- Matching notes for '{keyword}' ---")
    for note in matches:
        preview = note["content"][:50] + "..." if len(note["content"]) > 50 else note["content"]
        print(f"  [{note['id']}] {note['title']} - {preview}")


def set_reminder():
    data = load_notes()
    try:
        nid = int(input("Enter note ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    note = next((n for n in data["notes"] if n["id"] == nid), None)
    if not note:
        print("Note not found.")
        return
    while True:
        dt_str = input("Enter reminder datetime (YYYY-MM-DD HH:MM): ").strip()
        if not dt_str:
            print("Cannot be empty.")
            continue
        try:
            datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid format. Use YYYY-MM-DD HH:MM (e.g. 2026-12-31 14:30).")
    note["reminder_at"] = dt_str
    save_notes(data)
    print(f"Reminder set for note #{nid} at {dt_str}.")


def clear_reminder():
    data = load_notes()
    try:
        nid = int(input("Enter note ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    note = next((n for n in data["notes"] if n["id"] == nid), None)
    if not note:
        print("Note not found.")
        return
    if not note.get("reminder_at"):
        print("No reminder set on this note.")
        return
    note["reminder_at"] = None
    save_notes(data)
    print("Reminder cleared.")


def check_reminders():
    data = load_notes()
    now = datetime.now()
    due = []
    for note in data["notes"]:
        r = note.get("reminder_at")
        if r:
            try:
                if datetime.strptime(r, "%Y-%m-%d %H:%M") <= now:
                    due.append(note)
            except ValueError:
                pass
    if due:
        print("--- Pending Reminders ---")
        for note in due:
            print(f"  [{note['id']}] {note['title']} -> due {note['reminder_at']}")
        print()


def main():
    check_reminders()
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. View Note Detail")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Search Notes")
        print("7. Set Reminder")
        print("8. Clear Reminder")
        print("9. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_all_notes()
        elif choice == "3":
            view_note_detail()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            search_notes()
        elif choice == "7":
            set_reminder()
        elif choice == "8":
            clear_reminder()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-9.")


if __name__ == "__main__":
    main()
