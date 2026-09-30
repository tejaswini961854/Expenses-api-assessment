# Expense Management REST API

## Project Setup Steps
1. Clone the repository.
2. Open your terminal and create a virtual environment: python -m venv .venv
3. Activate the virtual environment:
   - Windows: .venv\Scripts\activate
   - Mac/Linux: source .venv/bin/activate
4. Install the required dependencies: pip install -r requirements.txt

## PostgreSQL Configuration
1. Create a PostgreSQL database named expense_db.
2. Create a user expense_user with a secure password and grant all privileges on the database to this user.
3. Create a .env file in the root directory of the project with the following variables:
   - DB_NAME=expense_db
   - DB_USER=expense_user
   - DB_PASSWORD=your_actual_password
   - DB_HOST=localhost
   - DB_PORT=5432
   - SECRET_KEY=your_django_secret_key
   - DEBUG=True

## Migration Commands
Run the following commands to apply the database schema:
python manage.py makemigrations expenses_app
python manage.py migrate
python manage.py runserver

## Authentication Instructions
1. Register a new user by sending a POST request to /auth/register/ with username, email, and password.
2. Obtain a JWT token by sending a POST request to /auth/login/ with your username and password.
3. Copy the access token from the response.
4. Include this token in the headers of all subsequent API requests: Authorization: Bearer <your_access_token>.

## API Endpoints
- POST /api/expenses/: Create a new expense.
- GET /api/expenses/: List all expenses (Supports pagination, search by description, and filtering by category or payment method).
- GET /api/expenses/<id>/: Retrieve a specific expense.
- PUT /api/expenses/<id>/: Fully update an expense.
- PATCH /api/expenses/<id>/: Partially update an expense.
- DELETE /api/expenses/<id>/: Delete an expense.
- GET /api/expenses/summary/: Retrieve the total expense amount and a category-wise breakdown for the authenticated user.

## Steps to Run the Project
1. Create a superuser account to access the Django admin panel:
   python manage.py createsuperuser
2. Start the local development server:
   python manage.py runserver
3. Open a browser and navigate to http://127.0.0.1:8000/admin/.
4. Log in with your superuser credentials and create initial Expense Categories (e.g., Food, Travel, Shopping) before testing the expense creation endpoints.