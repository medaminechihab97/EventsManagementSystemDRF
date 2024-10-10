# EventsManagementSystemDRF



+----------------+        +----------------+
|     User       |        |     Event      |
+----------------+        +----------------+
| id (PK)        |        | id (PK)        |
| username       |        | title          |
| email          |        | description    |
| password       |        | start_date     |
| first_name     |        | end_date       |
| last_name      |        | location       |
| role           |        | capacity       |
+----------------+        | actual_attendees|
        |                 | organizer (FK)  |
        |                 +----------------+
        |                         |
        |                         |
        |               +---------+---------+
        |               |                   |
+----------------+      |     +----------------+
| User_Event     |      |     | Event_Waitlist |
+----------------+      |     +----------------+
| user_id (FK)   |      |     | event_id (FK)  |
| event_id (FK)  |      |     | user_id (FK)   |
+----------------+      |     +----------------+
                        |
                        |
                +----------------+
                | User_Waitlist  |
                +----------------+
                | user_id (FK)   |
                | event_id (FK)  |
                +----------------+
```

Relationships:

1. User to Event (Organizer):
   - One-to-Many: A User can organize many Events, but each Event has only one organizer.

2. User to Event (Attendees):
   - Many-to-Many: A User can attend many Events, and an Event can have many attendees.
   - This relationship is represented by the User_Event junction table.

3. User to Event (Waitlist):
   - Many-to-Many: A User can be on the waitlist for many Events, and an Event can have many users on its waitlist.
   - This relationship is represented by the User_Waitlist junction table.

Key Points:
- The User model extends Django's AbstractUser, adding a 'role' field.
- The Event model has fields for title, description, dates, location, capacity, and actual attendees.
- The organizer of an Event is represented by a foreign key to the User model.
- The attendees and waitlist relationships are represented using Many-to-Many fields, which Django translates into junction tables.

This ERD represents the core structure of your Events Management System, showing how Users and Events are related, including the concepts of event attendance and waitlisting.