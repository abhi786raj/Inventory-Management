
# Inventory Management API

## Description

This project is a RESTful API built with Django to manage inventory items. It includes features for user registration, authentication, and CRUD operations for inventory items.

## Technologies Used

- **Django** 5.1.1
- **Django REST Framework**
- **MySQL**
- **Redis** (for caching)
- **JWT Authentication**

## Setup

### Prerequisites

- Python 3.x
- Django
- MySQL
- Redis

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhi786raj/inventory_management.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd inventory_management
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Create a MySQL database named `inventory`.
   - Update the database settings in `settings.py` if needed.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### User Authentication
- **Register:** `POST /auth/register/`
- **Login:** `POST /auth/login/`
- **Logout:** `POST /auth/logout/`

### Inventory Items
- **List/Create Items:** `GET/POST /api/items/`
- **Retrieve/Update/Delete Item:** `GET/PUT/DELETE /api/items/<item_id>/`

## Logging

API requests are logged to `api.log` in the project directory for monitoring and debugging.

## Creating Fake Data

Creating Fake Data using:

```bash
python manage.py create_items.py
```


## Testing

Run the tests using:

```bash
python manage.py test
```

## Contributing

Feel free to contribute to this project. Create an issue or submit a pull request for any enhancements or bug fixes.
