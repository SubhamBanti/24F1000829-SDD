## Context

The current app is a 20-line Python script (`notes app`) that appends note text to `my_notes.txt` and reads it back. No structure, no editing, no deletion, no search, no reminders. The replacement will be a single-file Python script using JSON for persistent storage.

## Goals / Non-Goals

**Goals:**
- Structured JSON storage with fields: id, title, content, created_at, updated_at, reminder_at
- Full CRUD: create, list all, view detail, edit, delete (with confirmation)
- Search by keyword across title and content
- Reminder system: set/clear reminder datetime, show pending reminders on app startup
- Clean menu loop with numbered options and input validation
- Rename file to valid Python name `notes_app.py`

**Non-Goals:**
- No external dependencies (standard library only)
- No background notification daemon (CLI-only: reminders shown on startup)
- No GUI or web interface
- No database engine (flat JSON file is sufficient)

## Decisions

- **JSON over plain text**: Allows structured fields (id, title, content, timestamps, reminder). Simple to read/write, human-readable, and parseable.
- **Auto-increment integer IDs**: Simplest approach for a single-user CLI tool. UUID would be overkill.
- **Reminder check on startup only**: Since this is a CLI app that runs and exits, the natural time to check for reminders is when the app launches. All pending/overdue reminders are printed before the menu.
- **Single file**: Keep it simple — all functions in `notes_app.py`. No need for modules at this scale.
- **ISO datetime format**: `YYYY-MM-DD HH:MM` for user input; stored as `YYYY-MM-DD HH:MM:SS` for precision.

## Data Model

```json
{
  "next_id": 1,
  "notes": [
    {
      "id": 1,
      "title": "Meeting Notes",
      "content": "Discuss Q3 roadmap with team",
      "created_at": "2026-05-26 14:30:00",
      "updated_at": "2026-05-26 15:00:00",
      "reminder_at": "2026-05-27 09:00:00"
    }
  ]
}
```

## Function Design

| Function | Purpose |
|----------|---------|
| `load_notes()` | Read and parse `notes.json`, return data dict |
| `save_notes(data)` | Write data dict to `notes.json` |
| `add_note()` | Prompt title + content, create note with timestamps |
| `view_all_notes()` | List all notes with ID, title, and timestamp |
| `view_note_detail()` | Show full detail of one note by ID |
| `edit_note()` | Update title and/or content of a note by ID |
| `delete_note()` | Remove a note by ID with confirmation |
| `search_notes()` | Keyword search across title and content |
| `set_reminder()` | Set reminder_at on a note by ID |
| `clear_reminder()` | Remove reminder_at from a note by ID |
| `check_reminders()` | Print pending/overdue reminders on startup |
| `main()` | Menu loop and entry point |

## Menu Flow

```
--- Notes App ---
Pending reminders:
  [1] Meeting Notes → due 2026-05-27 09:00

1. Add Note
2. View All Notes
3. View Note Detail
4. Edit Note
5. Delete Note
6. Search Notes
7. Set Reminder
8. Clear Reminder
9. Exit
Choose:
```

## Risks / Trade-offs

- **File corruption risk**: If the app crashes during write, `notes.json` could be corrupted. Mitigation: write is a single atomic write with `json.dump` — minimal risk for a CLI app.
- **No concurrent access**: This is single-user/single-process. No locking needed.
- **Startup-only reminders**: If the user doesn't launch the app, reminders won't fire. This is an accepted limitation of a CLI tool.
