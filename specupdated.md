# Events Management System

## Project Overview

The Events Management System is a web-based application that allows users to create, manage, and participate in events. It provides features for user authentication, event creation, event listing, and event participation management.

## Key Features

1. User Management
   - User registration (signup)
   - User authentication (signin)
   - Role-based access control (User and Admin roles)
   - User profile management

2. Event Management
   - Create new events
   - List all events
   - View event details
   - Update event information
   - Delete events
   - Join events
   - Manage event capacity
   - View event waitlist

3. Advanced Event Listing
   - Pagination
   - Filtering
   - Searching
   - Ordering
   - View upcoming events

4. API Documentation
   - Swagger UI
   - ReDoc

## Technical Specifications

### Backend Framework
- Django
- Django REST Framework

### Authentication
- JSON Web Tokens (JWT) using SimpleJWT

### Database
- Default: SQLite (can be easily switched to other databases supported by Django)

### API Endpoints

1. User Management
   - POST /api/signup/: User registration
   - POST /api/signin/: User login (token obtainment)
   - GET /api/user/: List all users (Admin only)
   - GET /api/user/<int:pk>/: Retrieve user details
   - PUT /api/user/<int:pk>/update/: Update user information
   - DELETE /api/user/<int:pk>/delete/: Delete user (Admin only)
   - POST /api/user/<int:pk>/assign_admin_role/: Assign admin role to a user (Admin only)

2. Event Management
   - GET /api/event/getEventList/: List all events
   - POST /api/event/createNewEvent/: Create a new event
   - GET /api/event/getEventById/<int:pk>/: Retrieve event details
   - PUT /api/event/updateEvent/<int:pk>: Update event information
   - DELETE /api/event/deleteEvent/<int:pk>: Delete an event
   - POST /api/events/<int:pk>/join/: Join an event
   - GET /api/events/<int:pk>/waitlist/: View event waitlist
   - POST /api/events/<int:pk>/manage-capacity/: Manage event capacity
   - GET /api/events/upcoming/: List upcoming events

3. API Documentation
   - GET /api/swagger/: Swagger UI
   - GET /api/redoc/: ReDoc documentation

### Models

1. User Model
   - Extends Django's AbstractUser
   - Fields: username, email, password, role

2. Event Model
   - Fields: title, description, start_date, end_date, organizer, location, capacity, attendees, waitlist, actual_attendees

### Permissions

- IsAuthenticatedAndHasRoleAdmin: For admin-only actions
- IsAuthenticatedAndHasRoleUser: For user-specific actions
- IsEventOwner: For event owner-specific actions

### Filtering and Searching

- Events can be filtered by title, start_date, end_date, location, and organizer
- Search functionality for events based on title, description, and location
- Ordering of events by start_date, end_date, and capacity

### Pagination

- Default page size: 10 items
- Customizable page size (up to 100 items per page)

## Code Structure

The project follows a standard Django project structure with a main app called 'events'.


## Setup and Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`

## API Usage

Refer to the Swagger UI (/api/swagger/) or ReDoc (/api/redoc/) for detailed API documentation and usage instructions.

## Future Enhancements

1. Implement email notifications for event updates and reminders
2. Add support for recurring events
3. Integrate with external calendar services (Google Calendar, iCal)
4. Implement a rating and review system for events
5. Add support for event categories and tags
6. Implement a recommendation system for events based on user preferences and past attendance
