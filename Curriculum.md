# 🧱 Backend Foundations with Python Bootcamp

**Goal:** Build strong backend development fundamentals using Python, with a focus on understanding *how backends work under the hood* — not just using frameworks.

---

## 🧩 Python & Object-Oriented Programming (OOP)

### 🎯 Learning Objectives
- Gain strong command of Python fundamentals.
- Understand software structure, reusability, and abstraction using OOP.
- Learn clean code practices, version control, and basic testing.

### 📘 Topics

#### **Python Fundamentals**
- Python syntax recap: variables, loops, conditionals, functions  
- Built-in data structures: lists, tuples, sets, dictionaries  
- File I/O: reading/writing files  
- Modules and packages  
- Virtual environments (`venv`, `pip`)  
- Error handling and debugging (`try/except`, `pdb`)  
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
- Introduction to type hints and `mypy`  
- Understanding how Python executes code (import system, interpreter)  

🧩 **Mini Project:**  
Extend the Library Management System with logging, input validation, and unit tests.

---

## 🌐 HTTP & REST APIs (From Scratch)

### 🎯 Learning Objectives
- Understand how the web works (HTTP, DNS, ports, etc.)
- Learn the principles of RESTful API design.
- Build simple web servers and APIs using only Python’s standard library (no frameworks).

### 📘 Topics

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

### 📘 Topics

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

## ⚙️ Advanced Backend Concepts

### 🎯 Learning Objectives
- Understand caching and background task processing.
- Learn to optimize API performance with caching and rate limiting.
- Implement lightweight concurrency and async concepts without frameworks.

### 📘 Topics

#### **Caching**
- Why caching matters (speed & scalability)  
- Types of caching: in-memory, file-based, distributed  
- Implementing in-memory caching with Python dictionaries and TTL  
- Introduction to Redis (conceptually, optional usage)  
- Cache invalidation strategies  

🧩 **Mini Project:**  
Add caching to your Bookstore API to speed up fetching popular books or frequent queries.

---

#### **Background Task Processing**
- Synchronous vs asynchronous operations  
- Basics of concurrency: threads, processes, async I/O  
- Implementing background jobs using threads or queues  
- Task scheduling concepts (delayed tasks, retry mechanisms)  
- Introduction to message queues (conceptual overview of RabbitMQ, Celery)  

🧩 **Mini Project:**  
Enhance your API to handle **email notifications or report generation** in the background using threads or async tasks.

---

#### **Rate Limiting & Request Control**
- Importance of rate limiting (protection & fairness)  
- Implementing request counters with dictionaries or Redis  
- Fixed window vs sliding window algorithms  
- Adding rate limiting to your API endpoints  
- Error responses for rate limits (429 Too Many Requests)  

🧩 **Mini Project:**  
Add a **Rate Limiting Middleware** to your API that limits users to a specific number of requests per minute.

---

#### **Putting It All Together**
- Combine caching, background tasks, and rate limiting  
- Logging and monitoring performance metrics  
- Configuring environment variables and secrets  
- Graceful shutdown and process management  

🧩 **Mini Project:**  
Integrate all these features into your existing API to simulate a **production-grade backend**.

---

## 🚀 DevOps & Deployment Essentials

### 🎯 Learning Objectives
- Understand the basics of DevOps workflows for backend engineers.
- Learn how to containerize and deploy Python applications.
- Build a simple CI/CD pipeline for automated testing and deployment.

### 📘 Topics

#### **Software Deployment & DevOps Overview**
- What is DevOps and why it matters  
- Continuous Integration vs Continuous Delivery vs Continuous Deployment  
- Understanding deployment environments (dev, staging, prod)  
- Environment variables and secrets management  
- Configuration management and `.env` files  

---

#### **Docker & Containerization**
- What containers are and why they’re useful  
- Installing and using Docker  
- Writing a basic `Dockerfile` for a Python app  
- Using `.dockerignore` and multi-stage builds  
- Running containers and exposing ports  
- Using `docker-compose` to run app + database  

🧩 **Mini Project:**  
Dockerize your **Bookstore API** — containerize both the API and database and run them together with `docker-compose`.

---

#### **CI/CD Pipelines**
- Introduction to CI/CD workflows  
- Setting up automated tests with GitHub Actions or GitLab CI  
- Running linting and tests automatically on push or pull request  
- Building and deploying containers automatically  
- Version tagging and release automation  

🧩 **Mini Project:**  
Set up a **CI/CD pipeline** that:
- Runs tests on every commit  
- Builds a Docker image automatically  
- Deploys to a staging environment after successful build  

---

#### **Monitoring & Logging Basics**
- Centralized logging and log levels  
- Application health checks and uptime monitoring  
- Error tracking (conceptual introduction to tools like Sentry or Prometheus)  
- Rollbacks and safe deployments  

🧩 **Mini Project:**  
Add **logging, error tracking, and a health check endpoint** to your deployed API.

---

## 🧠 Capstone Project

### 🎯 Learning Objectives
- Apply all learned concepts to build a complete, deployable backend system.
- Demonstrate proficiency in database integration, caching, async tasks, and deployment.
- Present a production-ready project with DevOps best practices.

### 📘 Topics

#### **Project Planning & Design**
- Define your project scope (choose one idea below)  
- Design database schema and architecture  
- Draft API documentation (OpenAPI/Swagger-style)  
- Set up Git repository and CI pipeline  

💡 **Suggested Capstone Ideas:**
- Task Manager API  
- Expense Tracker API  
- Student Result Portal  
- Event Registration API  
- Inventory Management System  
- News Aggregation API with caching, rate limiting, and background tasks  

---

#### **Implementation**
- Develop complete CRUD endpoints  
- Integrate caching, rate limiting, background processing  
- Containerize and deploy using Docker  
- Add automated testing and CI/CD pipeline  

---

#### **Finishing & Presentation**
- Refactor for clean architecture  
- Add comprehensive README and API documentation  
- Final code review and peer evaluation  
- Deploy final version to cloud or staging environment  

🎓 **Outcome:**  
Learners will have a **fully functional, tested, containerized, and deployed backend API** — complete with caching, rate limiting, background processing, and a CI/CD workflow.

---

## 🧰 Tools Used Throughout
- Python 3.11+  
- SQLite or PostgreSQL  
- Git & GitHub  
- `pytest`  
- `curl` / `httpie`  
- Docker & Docker Compose  
- GitHub Actions or GitLab CI  
- Redis (optional for caching/rate limiting)  
- VSCode or PyCharm  

---
