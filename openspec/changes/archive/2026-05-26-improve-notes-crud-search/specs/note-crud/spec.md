## ADDED Requirements

### Requirement: User can create a note
The system SHALL allow users to create a new note with a title and content body. Each note SHALL be assigned a unique auto-incrementing ID and SHALL record the creation timestamp.

#### Scenario: Create note with title and content
- **WHEN** user selects "Add Note" and enters a title and content
- **THEN** the note is saved with a unique ID, current timestamp, and displayed in the notes list

#### Scenario: Create note with empty title
- **WHEN** user enters an empty title
- **THEN** the system SHALL prompt again until a non-empty title is provided

### Requirement: User can view all notes
The system SHALL display all saved notes in a numbered list showing ID, title, and creation date.

#### Scenario: View notes when notes exist
- **WHEN** user selects "View All Notes" and notes exist
- **THEN** the system displays each note with its ID, title, and creation date

#### Scenario: View notes when no notes exist
- **WHEN** user selects "View All Notes" and no notes exist
- **THEN** the system displays "No notes found."

### Requirement: User can view a single note detail
The system SHALL display the full details of a single note including ID, title, content, created_at, updated_at, and reminder status.

#### Scenario: View note detail by valid ID
- **WHEN** user selects "View Note Detail" and enters a valid note ID
- **THEN** the system displays the full note details

#### Scenario: View note detail with invalid ID
- **WHEN** user enters a non-existent note ID
- **THEN** the system displays an error message

### Requirement: User can edit a note
The system SHALL allow users to update the title and/or content of an existing note by ID. The updated_at timestamp SHALL be refreshed on save.

#### Scenario: Edit note title and content
- **WHEN** user selects "Edit Note", enters a valid ID, and provides new title and content
- **THEN** the note is updated with the new values and the updated_at timestamp is refreshed

#### Scenario: Edit note with invalid ID
- **WHEN** user enters a non-existent note ID for editing
- **THEN** the system displays an error message

### Requirement: User can delete a note
The system SHALL allow users to delete a note by ID after showing a confirmation prompt with the note's title.

#### Scenario: Delete note with confirmation
- **WHEN** user selects "Delete Note", enters a valid ID, and confirms deletion
- **THEN** the note is permanently removed from storage

#### Scenario: Delete note cancelled
- **WHEN** user selects "Delete Note" and does not confirm
- **THEN** the note is not deleted and the user returns to the menu

#### Scenario: Delete note with invalid ID
- **WHEN** user enters a non-existent note ID for deletion
- **THEN** the system displays an error message
