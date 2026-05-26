## Why

The current Notes App only supports adding and viewing notes as plain text with no structure. There's no way to edit, delete, search, or set reminders. Users need a full-featured CLI notes tool with persistent structured storage, complete CRUD operations, full-text search, and reminder management.

## What Changes

- Switch storage from plain text (`my_notes.txt`) to structured JSON (`notes.json`)
- Add **title + content** fields (instead of just a single body)
- Add **Edit Note** (update title and/or content)
- Add **Delete Note** (with confirmation prompt)
- Add **Search Notes** (keyword search across title & content)
- Add **timestamps** — `created_at` and `updated_at` on every note
- Add **Reminders** — set/clear reminder datetime on a note; show pending reminders on app startup
- Rename file from `notes app` to `notes_app.py`
- Improve menu with numbered options and input validation

## Capabilities

### New Capabilities
- `note-crud`: Create, read, update, and delete notes with structured fields (title, content, timestamps)
- `note-search`: Full-text keyword search across note titles and content
- `note-reminders`: Set, clear, and display reminders with date/time alerts on app startup

### Modified Capabilities
*(no existing specs to modify)*

## Impact

- **File removed**: `notes app` (old script)
- **File created**: `notes_app.py` (new implementation)
- **Storage file**: `notes.json` (auto-generated, replaces `my_notes.txt`)
- No external dependencies — uses only Python standard library (`json`, `datetime`)
