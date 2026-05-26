## ADDED Requirements

### Requirement: User can set a reminder on a note
The system SHALL allow users to set a reminder datetime on an existing note. The user SHALL enter the reminder in `YYYY-MM-DD HH:MM` format.

#### Scenario: Set reminder on existing note
- **WHEN** user selects "Set Reminder", enters a valid note ID, and a valid datetime string
- **THEN** the note's reminder_at field is set and confirmation is displayed

#### Scenario: Set reminder with invalid datetime
- **WHEN** user enters an invalid datetime format
- **THEN** the system displays an error and prompts again

#### Scenario: Set reminder on non-existent note
- **WHEN** user enters a non-existent note ID
- **THEN** the system displays an error message

### Requirement: User can clear a reminder on a note
The system SHALL allow users to clear (remove) the reminder from an existing note.

#### Scenario: Clear reminder on existing note
- **WHEN** user selects "Clear Reminder", enters a valid note ID that has a reminder set
- **THEN** the note's reminder_at field is cleared

#### Scenario: Clear reminder on note without reminder
- **WHEN** user selects "Clear Reminder" on a note that has no reminder
- **THEN** the system displays a message that no reminder is set

### Requirement: System shows pending reminders on startup
When the application starts, the system SHALL check all notes for reminders whose datetime has passed or is due now, and display them before the menu.

#### Scenario: Pending reminders exist on startup
- **WHEN** the app starts and one or more notes have reminder_at ≤ current datetime
- **THEN** the system displays each reminder with note ID, title, and due datetime before the menu

#### Scenario: No pending reminders on startup
- **WHEN** the app starts and no notes have pending reminders
- **THEN** the system proceeds directly to the menu without showing reminders
