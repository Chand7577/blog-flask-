# Simple Flask Authentication App

This is a simple authentication system built using Flask. It includes user registration and login functionality with password hashing.

## Development Status

This project is still under development.

## Features

- Uses Jinja templating engine for rendering dynamic HTML
- User Registration
- User Login
- Password Hashing with `werkzeug.security`
- Session Management using Flask

## Prerequisites

Make sure you have Python installed (preferably Python 3.7+).

## Installation

1. Clone this repository:
   ```sh
     git clone https://github.com/Chand7577/blog-flask-.git
     cd blog-flask-
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Folder Structure

```
blog-flask-/
│── app.py               # Main Flask app
│── templates/           # HTML templates
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

## Dependencies

- Flask
- Flask-Login
- Flask-WTF
- Werkzeug (hashing)
- SQLAlchemy






