## ADDED Requirements

### Requirement: User can search notes by keyword
The system SHALL allow users to search across note titles and content using a keyword. The search SHALL be case-insensitive and return all matching notes with their ID, title, and a content preview.

#### Scenario: Search finds matching notes
- **WHEN** user selects "Search Notes" and enters a keyword that matches one or more note titles or content
- **THEN** the system displays each matching note with its ID, title, and first 50 characters of content

#### Scenario: Search finds no matches
- **WHEN** user enters a keyword that does not match any note
- **THEN** the system displays "No matching notes found."

#### Scenario: Search with empty keyword
- **WHEN** user enters an empty keyword
- **THEN** the system SHALL prompt again until a non-empty keyword is provided

#### Scenario: Search when no notes exist
- **WHEN** user selects "Search Notes" and no notes exist
- **THEN** the system displays "No notes found yet."
