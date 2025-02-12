# **FastAPI-Based Educational Platform - Detailed Documentation**

## **1. Introduction**
This documentation provides a comprehensive overview of the FastAPI-based educational platform designed for user authentication, role-based access control, assignment management, and faculty review functionalities.

## **2. Project Overview**
The platform enables students and faculty to interact through a structured API-based system, allowing:
- User Registration and Login
- Role-Based Access Control (RBAC) for Students and Faculty
- Assignment Submission by Students
- Assignment Review and Feedback by Faculty
- User Management by Admin

## **3. Technologies Used**
- **Backend:** FastAPI, Python 3.10+
- **Database:** PostgreSQL (or SQLite for development/testing)
- **Authentication:** JSON Web Tokens (JWT) using `python-jose`
- **Server:** Uvicorn
- **ORM:** SQLAlchemy
- **Middleware:** CORS
- **Testing:** Postman

---

## **4. Installation and Setup**
### **4.1 Prerequisites**
- Python 3.10+
- PostgreSQL (for production) or SQLite (for local testing)
- Virtual Environment

### **4.2 Installation Steps**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/fastapi-edu-platform.git
   cd fastapi-edu-platform
   ```
2. Create a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure the `.env` file with database credentials.
5. Run the migrations:
   ```sh
   alembic upgrade head
   ```
6. Start the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```
7. Access the API documentation at `http://127.0.0.1:8000/docs`.

---

## **5. API Endpoints**
### **5.1 Authentication**
#### **User Registration**
- **Endpoint:** `POST /register`
- **Request Body:**
  ```json
  {
    "username": "john_doe",
    "password": "securepassword",
    "role": "student"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully"
  }
  ```

#### **User Login**
- **Endpoint:** `POST /login`
- **Request Body:**
  ```json
  {
    "username": "john_doe",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "eyJhbGciOiJI...",
    "token_type": "bearer"
  }
  ```

---

### **5.2 Assignments Management**
#### **Submit Assignment (Student Only)**
- **Endpoint:** `POST /assignments`
- **Headers:**
  ```json
  {"Authorization": "Bearer <token>"}
  ```
- **Request Body:**
  ```json
  {
    "title": "Machine Learning Basics",
    "description": "Introduction to ML",
    "file_url": "https://example.com/assignment1.pdf"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Assignment submitted successfully"
  }
  ```

#### **Get All Assignments (Faculty & Student)**
- **Endpoint:** `GET /assignments`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Machine Learning Basics",
      "submitted_by": "john_doe"
    }
  ]
  ```

#### **Review Assignment (Faculty Only)**
- **Endpoint:** `POST /assignments/review/{assignment_id}`
- **Request Body:**
  ```json
  {
    "grade": "A",
    "feedback": "Well done!"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Review submitted successfully"
  }
  ```

---

### **5.3 User Management**
#### **Get All Users (Admin Only)**
- **Endpoint:** `GET /users`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "username": "john_doe",
      "role": "student"
    }
  ]
  ```

#### **Delete User (Admin Only)**
- **Endpoint:** `DELETE /users/{user_id}`
- **Response:**
  ```json
  {
    "message": "User deleted successfully"
  }
  ```

---

## **6. Database Schema**
### **Users Table**
| Column  | Type       | Description             |
|---------|-----------|-------------------------|
| id      | Integer   | Primary Key             |
| username | String   | Unique Username         |
| password | String   | Hashed Password         |
| role    | String    | `student` or `faculty`  |

### **Assignments Table**
| Column   | Type     | Description          |
|----------|---------|----------------------|
| id       | Integer | Primary Key          |
| title    | String  | Assignment Title     |
| description | Text  | Assignment Details  |
| file_url | String  | File Storage URL     |
| submitted_by | Integer | Foreign Key (User) |

### **Reviews Table**
| Column      | Type     | Description            |
|------------|---------|------------------------|
| id         | Integer | Primary Key            |
| assignment_id | Integer | Foreign Key (Assignment) |
| grade      | String  | Assigned Grade        |
| feedback   | Text    | Faculty Comments      |
| reviewed_by | Integer | Foreign Key (User)   |

---

## **7. Security Measures**
- **JWT Authentication** to secure API endpoints
- **Role-Based Access Control (RBAC)** to restrict user actions
- **Password Hashing** with bcrypt for secure storage
- **CORS Middleware** to prevent cross-origin issues
- **SQLAlchemy ORM** to prevent SQL injection

---

## **8. Testing & Deployment**
### **8.1 Running Tests**
- Install pytest:
  ```sh
  pip install pytest
  ```
- Run tests:
  ```sh
  pytest
  ```

### **8.2 Deployment**
- Deploy using **Docker**, **Heroku**, or **AWS Lambda**.
- Configure `gunicorn` for production.

---

## **9. Conclusion**
This FastAPI-based platform efficiently manages user authentication, assignment submissions, and faculty reviews, ensuring a seamless experience for students and faculty.

---

### **10. Future Enhancements**
- **File Upload Support** instead of URLs
- **Email Notifications** for feedback
- **Analytics Dashboard** for performance tracking
- **Mobile App Integration**

