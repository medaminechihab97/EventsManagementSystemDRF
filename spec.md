# Event Management System: Project Overview and API Documentation

## Project Background and Motivation

The Event Management System project was chosen for several compelling reasons:

1. **Personal Passion**: The project resonates with my experience in organizing events for university associations. It allows me to leverage my practical knowledge and transform it into a digital solution.

2. **Real-World Application**: This project provides hands-on experience with a real-life scenario, bridging the gap between academic learning and industry needs.

3. **Skill Development**: Implementing this system allows for the practical application of various technologies and concepts, including:
   - RESTful API design
   - User authentication and authorization
   - Database modeling and management
   - Scalable system architecture

4. **Problem-Solving Opportunity**: Event management often involves complex logistics. This project presents an opportunity to solve real-world challenges through technology.

5. **Market Relevance**: With the growing demand for digital solutions in event management, this project aligns well with current industry trends.

6. **Extensibility**: The core system can be expanded to include features like ticketing, analytics, or integration with other platforms, providing opportunities for continuous learning and development.

## API Overview

The Event Management System API provides a comprehensive set of endpoints for managing users, events, and related functionalities. Here's an overview of the main components:

### User Management
- User registration (signup)
- User authentication (signin)
- User profile retrieval and updates
- Admin role assignment

### Event Management
- Create, read, update, and delete events
- Join events
- Manage event capacity
- Handle waitlists

### Key Features
- Role-based access control (User and Admin roles)
- JWT-based authentication
- Waitlist management for events at capacity
- Dynamic capacity management

## Project Planning and Specifications

### 1. System Architecture
- Backend: Django with Django REST Framework
- Database: MySQL
- Authentication: JWT (JSON Web Tokens)

### 2. Data Models
- User Model (Extended Django's AbstractUser)
  - Fields: username, email, role
- Event Model
  - Fields: title, description, start_date, end_date, organizer, location, capacity, attendees, waitlist

### 3. API Endpoints

#### User Management
- POST /api/signup/: User registration
- POST /api/signin/: User authentication
- GET /api/user/: List all users (Admin only)
- GET /api/user/<id>/: Retrieve user details
- PUT /api/user/<id>/update/: Update user details
- DELETE /api/user/<id>/delete/: Delete user
- POST /api/user/<id>/assign_admin_role/: Assign admin role to user

#### Event Management
- GET /api/event/getEventList/: List all events
- POST /api/event/createNewEvent/: Create a new event
- GET /api/event/getEventById/<id>/: Retrieve event details
- PUT /api/event/updateEvent/<id>: Update event details
- DELETE /api/event/deleteEvent/<id>: Delete event
- POST /api/events/<id>/join/: Join an event
- GET /api/events/<id>/waitlist/: Get event waitlist
- POST /api/events/<id>/manage-capacity/: Manage event capacity

### 4. Security Measures
- Custom permission classes for role-based access control
- JWT for secure authentication
- Input validation and sanitization

### 5. Documentation
- API documentation using Swagger and ReDoc

### 6. Future Enhancements
- Implement email notifications
- Add search and filtering capabilities for events
- Integrate with payment gateways for paid events
- Develop a front-end application consuming the API

### 7. Testing Strategy
- Implement unit tests for models, serializers, and views
- Conduct integration tests for API endpoints
- Perform security testing (e.g., penetration testing)

## Conclusion

The Event Management System project presents a comprehensive solution for digital event organization. By combining personal passion with practical application, this project serves as an excellent platform for skill development and creating a valuable tool for event organizers.

