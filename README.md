
[CHANGES](webapp/CHANGES.rst)

# Library Management System

## Description  
A simple application for managing a library where users can search and borrow books, while administrators can manage books and users.

---

## Features  
- **Anonymous Users**: Can browse available books.  
- **Registered Users**: Can search for and borrow books.  
- **Administrators**:  
  - Manage books (add, remove, update).  
  - Manage user permissions.  
- **Authentication**: JWT-based authentication for securing API.  
- **Documentation**:  
  - Swagger UI for API testing.  
  - Sphinx-generated RST documentation.  
- **Deployment**: Prepared for deployment using Docker and Render.com.  
- **Pagination and Filtering**: Books list supports filtering and pagination.  
- **Testing**: Unit and integration tests for models, views, and serializers.

---

## Technologies  
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL  
- **Deployment**: Docker, Render.com  
- **Documentation**: Swagger, Sphinx RST  
- **Testing**: Pytest
- **Tools**: Git  

---

## Live Demo

The application is deployed and available here:

- [Live Demo on Render](https://library-management-system-app-a4tc.onrender.com/)

---

## API Documentation

- **Swagger UI**: `/api/v1/`
- **Redoc UI**: `/api/v1/redoc/`
- **Production Documentation**: [Swagger UI](https://library-management-system-app-a4tc.onrender.com/api/v1/) or [Redoc UI](https://library-management-system-app-a4tc.onrender.com/api/v1/redoc/)

---

## Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/airyou-code/library_management_system.git
cd library-management-system
````

### 2. Setup Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file based on `.env.example` and update your database credentials and other settings.

### 4. Run Database Migrations

```bash
python webapp/manage.py migrate
```

### 5. Start the Server

```bash
python webapp/manage.py runserver
```

### 6. Access the Application

- Web: `http://127.0.0.1:8000/`

---

## Docker Deployment

### 1. Build the Docker Image

```bash
docker build -t library-system .
```

### 2. Run the Docker Container

```bash
docker-compose up
```

### 3. Access the Application

- Web: `http://localhost:8000`

## Testing

### Run Tests

```bash
pytest
```

---

## Folder Structure

```
➜ tree --gitignore -L 3
.
├── CHANGES.rst
├── api
│   ├── __init__.py
│   ├── urls.py
│   ├── v1
│   │   ├── __init__.py
│   │   └── urls.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── docs
│   ├── Makefile
│   ├── README.md
│   ├── _build
│   │   ├── doctrees
│   │   └── html
│   ├── _static
│   ├── _templates
│   ├── make.bat
│   ├── requirements.txt
│   ├── server_docs.py
│   └── source
│       ├── changelog.rst
│       ├── conf.py
│       └── index.rst
├── library
│   ├── __init__.py
│   ├── admin.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── users
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── webapp
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Credits

- **Django REST Framework**
- **Docker**
- **PostgreSQL**

---

## License

This project is licensed under the MIT License.