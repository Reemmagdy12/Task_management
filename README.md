# Task_management
Task Management API

Overview

Task Management API is a backend service built with Django and Django REST Framework (DRF) to manage tasks effectively. It provides endpoints for user authentication, task creation, updates, deletion, and filtering. Each user can manage their own tasks without accessing others' data, ensuring privacy and security.

Features

User Management:

User registration, login, and secure authentication (JWT).

Each user has a unique username, email, and password.


Task Management:

Create, read, update, and delete tasks.

Task attributes include Title, Description, Due Date, Priority Level (Low, Medium, High), and Status (Pending, Completed).

Mark tasks as complete or incomplete, with a timestamp for completion.

Validation for due dates and priority levels.


Task Filters and Sorting:

Filter tasks by status, priority level, and due date.

Sort tasks by due date or priority.


Access Control:

Users can only manage their own tasks.

Permission checks to prevent unauthorized access.



Technical Stack

Backend Framework: Django, Django REST Framework (DRF)

Authentication: Django's built-in authentication and JWT (via DRF SimpleJWT)

Database: SQLite (default) – easily configurable to PostgreSQL, MySQL, etc.

Deployment: Deployed on platforms like Heroku or PythonAnywhere.


Endpoints Overview

User Management:

/api/users/ - Register a new user.

/api/token/ - Obtain a JWT token.

/api/token/refresh/ - Refresh JWT token.


Task Management:

/api/tasks/ - Create a task or list all tasks (for the logged-in user).

/api/tasks/<id>/ - Retrieve, update, or delete a specific task.


Filters & Sorting:

Filter tasks by status, priority, or due_date.

Sort tasks by due_date or priority.



Setup Instructions

1. Clone the repository:

git clone https://github.com/Reemmagdy12/Task_management.git
cd task_management


2. Install dependencies:

pip install -r requirements.txt


3. Apply migrations:

python manage.py migrate


4. Run the server:

python manage.py runserver



Deployment

Ensure the database is configured for production (e.g., PostgreSQL).

Set up environment variables for secret keys and database settings.

Deploy to Heroku, PythonAnywhere, or your preferred platform.


License

This project is open-source and free to use.
