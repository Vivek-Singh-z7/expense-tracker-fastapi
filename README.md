# Expense Tracker API

A backend Expense Tracker application built using **FastAPI** and **PostgreSQL**.
The project provides RESTful APIs to create, read, update, and delete expense records.

## 🚀 Features

* Create new expenses
* Get all expenses
* Get a single expense by ID
* Update an existing expense
* Delete an expense
* Input validation using Pydantic
* PostgreSQL database integration
* CORS configuration
* Simple frontend interface
* RESTful API structure
* Interactive API documentation using Swagger UI

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **PostgreSQL**
* **Pydantic**
* **psycopg**
* **HTML**
* **CSS**
* **JavaScript**

## 📁 Project Structure

```text
expense_tracker_with_fastapi/
expense_tracker_with_fastapi/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
├── conn/
│   ├── __init__.py
│   └── db.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── schemas/
│   ├── __init__.py
│   └── expense_schema.py
│
└── service/
    ├── __init__.py
    ├── add_expense.py
    ├── get_data.py
    ├── update.py
    └── delete.py
```

## 🔗 API Endpoints

| Method   | Endpoint                    | Description          |
| -------- | --------------------------- | -------------------- |
| `POST`   | `/expense_tracker_app`      | Create a new expense |
| `GET`    | `/expense_tracker_app`      | Get all expenses     |
| `GET`    | `/expense_tracker_app/{id}` | Get an expense by ID |
| `PUT`    | `/expense_tracker_app/{id}` | Update an expense    |
| `DELETE` | `/expense_tracker_app/{id}` | Delete an expense    |

## 📌 Expense Data

An expense contains information such as:

* Title
* Amount
* Category
* Expense date
* Expense ID

## 🗄️ Database

The application uses **PostgreSQL** as the database.

The database stores expense records and allows the API to perform CRUD operations.

Database credentials should be configured locally and should **not** be committed to the repository.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd expense_tracker_with_fastapi
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn psycopg pydantic
```

### 5. Configure PostgreSQL

Create the required PostgreSQL database and configure your database connection details.

**Do not put your actual database password in this README or on GitHub.**

### 6. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## 🎯 Project Purpose

This project was built to practice backend development concepts including:

* REST API development
* CRUD operations
* Database integration
* Request validation
* API routing
* PostgreSQL queries
* FastAPI project structure
* Frontend and backend communication

## 🔮 Future Improvements

Possible future improvements include:

* User authentication
* JWT-based authorization
* User-specific expenses
* Expense filtering and pagination
* Expense statistics
* API deployment
* Production database configuration

## 👨‍💻 Author

**Vivek Singh**
