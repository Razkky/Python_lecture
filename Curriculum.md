# 🧱 Backend Foundations with Python Bootcamp

**Goal:** Build strong backend development fundamentals using Python, with a focus on understanding *how backends work under the hood* — not just using frameworks.

---

## 🗓️ Python & Object-Oriented Programming (OOP)

### 🎯 Learning Objectives
- Gain strong command of Python fundamentals.
- Understand software structure, reusability, and abstraction using OOP.
- Learn clean code practices, version control, and basic testing.

### 📘 Topics by Week

#### **Python Fundamentals**
- Python syntax recap: variables, loops, conditionals, functions  
- Built-in data structures: lists, tuples, sets, dictionaries  
- File I/O: reading/writing files  
- Modules and packages  
- Virtual environments (`venv`, `pip`)  
- Error handling and debugging (`try/except`)  
- Command-line programs and user input  

🧩 **Mini Project:**  
Build a **Command-Line To-Do List Manager** (CRUD operations on a file).

---

#### **Deep Dive into OOP**
- Classes and objects  
- Instance vs class variables  
- Methods (instance, class, static)  
- Encapsulation and data hiding  
- Inheritance and polymorphism  
- Composition vs inheritance  
- Magic (dunder) methods (`__str__`, `__repr__`, `__len__`, etc.)  
- Designing modular, reusable code  

🧩 **Mini Project:**  
Create a **Library Management System** that manages books, members, and loans using OOP classes.

---

#### **Software Engineering Practices**
- Code organization and module structure  
- Introduction to unit testing (`unittest` or `pytest`)  
- Using Git & GitHub (branching, commits, pull requests)  
- Logging and configuration files  
- Introduction to type hints
- Understanding how Python executes code (import system, interpreter)  

🧩 **Mini Project:**  
Extend the Library Management System with logging, input validation, and unit tests.

---

## 🌐 HTTP & REST APIs (From Scratch)

### 🎯 Learning Objectives
- Understand how the web works (HTTP, DNS, ports, etc.)
- Learn the principles of RESTful API design.
- Build simple web servers and APIs using only Python’s standard library (no frameworks).

### 📘 Topics by Week

#### **Networking & HTTP Basics**
- What happens when you visit a URL  
- HTTP request/response structure (headers, methods, status codes)  
- HTTP verbs: GET, POST, PUT, DELETE  
- Building simple servers with Python’s `http.server`  
- Handling routes manually  
- Returning HTML and JSON responses  

🧩 **Mini Project:**  
Build a **Mini HTTP Server** that responds to specific routes with different messages.

---

#### **REST API Fundamentals**
- REST principles and resource-oriented design  
- JSON serialization/deserialization  
- Query parameters and path variables  
- Building REST APIs using only `http.server` or `BaseHTTPRequestHandler`  
- Handling POST and PUT data  
- Structuring code for multiple routes  

🧩 **Mini Project:**  
Create a **Simple Notes API** — store notes in memory, and expose endpoints:
- `GET /notes`  
- `POST /notes`  
- `PUT /notes/{id}`  
- `DELETE /notes/{id}`

---

#### **Error Handling, Testing, and API Design**
- Proper use of HTTP status codes  
- API error responses and validation  
- API documentation and testing with `curl` or `httpie`  
- Writing API tests with `pytest`  
- Separating business logic from transport logic (code structure)  

🧩 **Mini Project:**  
Enhance the Notes API to include:
- Error handling (404, 400, 500)  
- JSON file persistence  
- Automated tests  

---

## 🧮 Databases & CRUD APIs

### 🎯 Learning Objectives
- Learn database design and normalization.
- Write SQL queries and integrate Python with databases.
- Implement persistent CRUD APIs with real database storage.

### 📘 Topics by Week

#### **SQL and Relational Databases**
- Introduction to relational databases (SQLite, PostgreSQL)  
- Tables, primary keys, foreign keys  
- SELECT, INSERT, UPDATE, DELETE  
- Filtering, joins, aggregates  
- Designing schemas for small applications  
- Using SQLite from the terminal  

🧩 **Mini Project:**  
Design and query a **Student Management Database** — create tables for students, courses, and enrollments.

---

#### **Python + Databases Integration**
- Python DB-API basics (`sqlite3` module)  
- Writing SQL queries from Python code  
- Parameterized queries and SQL injection prevention  
- Building a small data access layer  
- Database connection management  
- CRUD operations from Python  

🧩 **Mini Project:**  
Integrate your **Student Management API** — expose endpoints to manage students and courses, backed by SQLite.

---

#### **Building Full CRUD APIs**
- Layered architecture: routes → services → repositories  
- Designing clean CRUD endpoints  
- Transactions and data consistency  
- Pagination, sorting, and filtering  
- Testing database-backed APIs  

🧩 **Mini Project:**  
Complete a **Bookstore CRUD API** with full database integration, input validation, and API tests.

---

## 🧠 Capstone Project

### 🎯 Learning Objectives
- Apply all learned concepts to build a complete backend project.
- Practice real-world project structure, testing, and documentation.
- Understand deployment readiness and teamwork using Git.

### 📘 Topics by Week

#### **Project Planning & Design**
- Brainstorm and define the project scope (choose one idea below)  
- API specification and documentation (OpenAPI/Swagger-style)  
- Database schema design  
- Setting up Git repo and base project structure  

💡 **Suggested Capstone Ideas:**
- Task Manager API  
- Expense Tracker API  
- Student Result Portal  
- Event Registration API  
- Inventory Management System  

---

#### **Implementation**
- Build core API endpoints (CRUD)  
- Implement database integration  
- Add error handling, logging, and config management  
- Write tests for major components  

---

#### **Finishing & Presentation**
- Refactor for clean architecture  
- Add documentation (README + API docs)  
- Conduct peer code reviews  
- Optional: containerize with Docker for local deployment  
- Final project presentation/demo  

🎓 **Outcome:**  
Learners will have a **fully functional, tested, and documented backend API** — built from scratch with Python and SQL, no frameworks.

---

## 🧰 Tools Used Throughout
- Python 3.11+  
- SQLite or PostgreSQL  
- Git & GitHub  
- `pytest`  
- `curl` / `httpie`  
- VSCode or PyCharm  

---
