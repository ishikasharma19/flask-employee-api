👩‍💼 Employee Management API (Flask + MySQL)
A Flask-based REST API for managing employee records using SQLAlchemy ORM and MySQL. This project supports adding and retrieving employee data and includes a basic frontend using Jinja templates.




📌 Features
✅ Add new employees via POST API
✅ Retrieve all employees via GET API
✅ Integrated with MySQL using SQLAlchemy ORM
✅ Simple frontend using Jinja templates
✅ Displays total number of employees
✅ Unique email constraint for each employee

🛠️ Tech Stack
Backend: Python, Flask, SQLAlchemy

Database: MySQL

Templating Engine: Jinja2

Tooling: Postman (API Testing), pip (Package Management)

📁 Project Structure
graphql
Copy code
employee_app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html         # HTML template using Jinja2
└── README.md              # Project documentation

🚀 Setup Instructions
Clone the Repository
Clone the project from GitHub to your local machine:
git clone https://github.com/yourusername/employee_app.git

Navigate into the Project Directory
cd employee_app

Create and Activate Virtual Environment

Create: python -m venv venv

Activate (Windows): venv\Scripts\activate

Install Dependencies
Run: pip install -r requirements.txt

Set Up MySQL

Install MySQL Workbench or XAMPP

Create a database named employee_db

Set your MySQL credentials in app.py

Run the Application
Execute: python app.py
Open http:url in your browser

📮 API Endpoints
➕ Add New Employee

Endpoint: POST /add_employee

Payload Format:

json
Copy code
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "HR",
  "joining_date": "2024-06-01"
}
📃 Get All Employees

Endpoint: GET /employees

Response Format:

json
Copy code
{
  "total_employees": 3,
  "employees": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "department": "HR",
      "joining_date": "2024-06-01"
    },
    ...
  ]
}










