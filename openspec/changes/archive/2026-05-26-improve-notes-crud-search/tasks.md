## 1. Core Setup

- [x] 1.1 Create `notes_app.py` with JSON load/save helpers (`load_notes`, `save_notes`)
- [x] 1.2 Remove old `notes app` file, add `notes.json` to `.gitignore`

## 2. CRUD Operations

- [x] 2.1 Implement `add_note()` — prompt for title + content, auto-generate ID and timestamps, save
- [x] 2.2 Implement `view_all_notes()` — display numbered list of notes with ID, title, creation date
- [x] 2.3 Implement `view_note_detail()` — display full details of a single note by ID
- [x] 2.4 Implement `edit_note()` — select note by ID, update title and/or content, refresh updated_at
- [x] 2.5 Implement `delete_note()` — select note by ID, show confirmation prompt, delete if confirmed

## 3. Search

- [x] 3.1 Implement `search_notes()` — keyword search across title and content (case-insensitive), display matching results with preview

## 4. Reminders

- [x] 4.1 Implement `set_reminder()` — set a reminder datetime on a note by ID with `YYYY-MM-DD HH:MM` format
- [x] 4.2 Implement `clear_reminder()` — remove reminder from a note by ID
- [x] 4.3 Implement `check_reminders()` — scan notes for pending/overdue reminders, display on startup

## 5. Menu and Integration

- [x] 5.1 Implement `main()` — menu loop with all 9 options, input validation, `if __name__` guard
- [x] 5.2 Verify app runs end-to-end: create, view, edit, search, set reminder, delete, exit
