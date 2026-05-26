# 24F1000829-SDD

Spec-Driven Development Workshop Project by **24F1000829** (Subham Das)

## Notes App

A CLI-based notes application with persistent JSON storage.

### Features

- **Create** — Add notes with title and content (auto-timestamped)
- **Read** — View all notes or see full detail of a single note
- **Update** — Edit title and/or content of existing notes
- **Delete** — Remove notes with confirmation prompt
- **Search** — Case-insensitive keyword search across titles and content
- **Reminders** — Set/clear date/time reminders (`YYYY-MM-DD HH:MM`); pending reminders shown on startup

### How to Run

```bash
python notes_app.py
```

### Menu

```
1. Add Note
2. View All Notes
3. View Note Detail
4. Edit Note
5. Delete Note
6. Search Notes
7. Set Reminder
8. Clear Reminder
9. Exit
```

### Storage

Notes are stored in `notes.json` (auto-generated, gitignored).
