# Python_Project
Python_Project
# Python Blog Application

## Description

This project is a Python Django-based blog application that allows users to register, log in, and manage their blog posts. Authenticated users can create, update, and delete their own posts, while all visitors can view published posts.

## Features

- User Registration and Authentication
- Create, Read, Update, and Delete (CRUD) operations for blog posts
- List view of all blog posts
- Detailed view for individual blog posts
- Basic styling using Bootstrap for a responsive design

## Installation

1. I created a Git repository with a README file

2. Clone the repository:

   ```bash
   git clone https://github.com/Nived/Python_Project.git
   cd Python_Project

3. Create and activate a virtual environment:
   python -m venv venv 
   venv\Scripts\activate

4. Install the required dependencies:
   pip install Django

5. Create the Django project and app:
  django-admin startproject Python_Project
  cd Python_project
  python manage.py startapp Project_app

6. Configure settings.py:
   Add 'Python_app' to the INSTALLED_APPS list in Python_Project/settings.py.

7. Python_app

   urls.py: Defines URL patterns that map to specific views, determining how users navigate through your application.

   views.py: Contains the logic that processes user requests and returns appropriate responses, often rendering templates.

   forms.py: Manages user input through forms, handling data validation and processing.

   models: Use models.py to define the database.

8. Apply migrations to set up the database:
   python manage.py makemigrations
   python manage.py migrate 

9. Create a superuser account:
   python manage.py createsuperuser

10. Start the development server:
   python manage.py runserver

11. Access the application:
   Open web browser and navigate to http://127.0.0.1:8000/ to view the blog.


Project Structure:

Python_app/
├── blog/
│   ├── migrations/
│   ├── templates/
    │   ├── blog/
            │   │   └── Blog.html/
            │   │   └── cong_delete.html/
            │   │   └── details.html/
            │   │   └── form.html/
    │   ├── Registration/
            │   │   └── login.html/
            │   │   └── register.html/
│   ├── _init_.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Python_project/
│   ├── _init_.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt