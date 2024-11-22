# **Notification API**
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Duannee/notifications_api/blob/main/LICENSE)

Welcome to the Notification API! This API is designed to manage different types of notifications using WebSocket connections for real-time notifications and HTTP requests for notifications related to events and courses. With a modular architecture and a well-tested approach, it ensures performance and organization.

---

## **Index**

1. [Overview](#overview)  
2. [Notification Types](#notification-types)  
   - [Content Interactions (WebSocket)](#content-interactions-websocket)  
   - [Courses (HTTP with Signals)](#courses-http-with-signals)  
   - [Events (HTTP with Signals)](#events-http-with-signals)  
3. [Technologies Used](#technologies-used)  
4. [Authentication](#authentication)  
5. [Available Routes](#available-routes)  
   - [Route Tags](#route-tags)  
   - [Course and Event Routes](#course-and-event-routes)  
   - [WebSocket Routes](#websocket-routes)  
6. [Testing](#testing)  
7. [Documentation](#documentation)  
8. [How to Contribute](#how-to-contribute)  
9. [Contact](#contact)  

---

## **Overview**

The API manages real-time notifications for content interactions, as well as notifications related to courses and events. We use **WebSocket** for instant messages and **HTTP** for notifications based on structural changes, such as course or event updates.

### Benefits:
- **Real-time notifications**: Provides a better user experience with instant updates.
- **Decoupled architecture**: Signals manage notifications related to courses and events.
- **Security**: Authentication with **JSON Web Token (JWT)**.
- **Performance**: **Redis database** for efficient temporary data storage.

---

## **Notification Types**

### **Content Interactions (WebSocket)**

The following notifications are sent in real-time via **WebSocket**:

1. **New comment on a post**  
   - Notifies participants when a new comment is added to a post.

2. **New like on a post**  
   - Notifies the post author when it receives a like.

3. **Reply to a comment**  
   - Notifies the original comment's author when someone replies.

4. **New like on a comment**  
   - Notifies the comment's author when it receives a like.

---

### **Courses (HTTP with Signals)**

Course-related notifications are handled via **HTTP**, using **Signals** to decouple the business logic from the API. Notifications include:

5. **New course available**  
   - Notifies users when a new course is created.

6. **Course update**  
   - Notifies enrolled users about changes, such as new modules or lessons.

---

### **Events (HTTP with Signals)**

Event notifications also use **Signals**, similar to course notifications. Notifications include:

7. **New event created**  
   - Notifies interested users about a new event.

8. **Event update**  
   - Notifies registered users when an event changes, such as date or location.

---

## **Technologies Used**

- **Language**: Python.  
- **Frameworks**: Django, Django Rest Framework (DRF).  
- **WebSocket**: Django Channels.  
- **Authentication**: JWT via Simple JWT.  
- **Database**: Redis.  
- **Documentation**: Swagger with DRF Spectacular.  

---

## **Authentication**

The API uses **JWT (JSON Web Token)** for authentication.

### How it works:
1. Login via `/api/token/` to get:
   - **Access Token**: Valid for 30 minutes.
   - **Refresh Token**: Valid for 7 days.

2. Use the **Access Token** in the request headers:  
   ```bash
   Authorization: Bearer <your token>

---

# Available Routes 
### Route Tags 
Routes are organized into tags for easier navigation:

- Token: Operations related to authentication.
- WebSocket: Explains how to connect via WebSocket.
- Course: Management and notifications for courses (HTTP).
- Event: Management and notifications for events (HTTP).

### Course and Event Routes 
Both resources (courses and events) have three main routes:

1. PATCH: Partially update a course/event.
2. PUT: Completely update a course/event.
3. POST: Create a new course/event.

### WebSocket Routes
- GET /api/ws/notification
  - Explains how to use real-time notifications via WebSocket.
To connect to the WebSocket:
1. Use the endpoint:
   ```perl
   ws://localhost:8000/ws/notifications/
   ```
2. Send the JWT token in the connection header.

---

# Testing
- The API is fully tested with unit tests and integration tests using:
  - Unittest: To validate individual functionalities.
  - TestCase: To simulate complete scenarios.

---

# Documentation
The complete API documentation was created with Swagger, using DRF Spectacular. It details all endpoints, usage examples, and expected responses.

Access the documentation at the link:
- [Notification API Doc](http://127.0.0.1:8000/api/notification/docs/)

---

# How to Contribute
1. Fork the repository.
2. Create a branch for your changes:
```bash
git checkout -b you-branch-name
```
3. Submit a pull request detailing your contributions.

---

# Contact
- Developer: **Duanne Moraes**
- Email: duannemoraes.dev@gmail.com
- Linkedin: [Duanne Moraes Linkedin](https://www.linkedin.com/in/duanne-moraes-7a0376278/)









