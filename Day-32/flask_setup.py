# ==========================================================
#                  FLASK SETUP NOTES
# ==========================================================

# ----------------------------------------------------------
# 1. What is Flask?
#
# Flask is a lightweight Python web framework used to build:
#
# - Websites
# - Web Applications
# - REST APIs
# - Backend Services
#
# It is simple, flexible, and beginner-friendly.
#
# Flask follows the WSGI (Web Server Gateway Interface)
# standard and is based on the Jinja2 template engine.

# ----------------------------------------------------------
# 2. Why Use Flask?
#
# Advantages:
#
# - Lightweight
# - Easy to learn
# - Fast development
# - Flexible architecture
# - Good for REST APIs
# - Large community support

# ----------------------------------------------------------
# 3. Install Flask
#
# Install Flask using pip:
#
# pip install flask
#
# Check installation:
#
# pip show flask
#
# Check version:
#
# flask --version

# ----------------------------------------------------------
# 4. Create a Project Folder
#
# Example:
#
# FlaskProject/
# │
# ├── app.py
# ├── templates/
# ├── static/
# └── venv/

# ----------------------------------------------------------
# 5. Create Virtual Environment (Recommended)
#
# Create:
#
# python -m venv venv
#
# Activate (Windows):
#
# venv\Scripts\activate
#
# Activate (Mac/Linux):
#
# source venv/bin/activate
#
# Deactivate:
#
# deactivate

# ----------------------------------------------------------
# 6. Install Flask Inside Virtual Environment
#
# pip install flask

# ----------------------------------------------------------
# 7. First Flask Program

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

# ----------------------------------------------------------
# 8. Explanation of First Program
#
# from flask import Flask
# Imports the Flask class.
#
# app = Flask(__name__)
# Creates the Flask application object.
#
# @app.route("/")
# Maps the URL "/" to the home() function.
#
# return
# Sends a response to the browser.
#
# app.run()
# Starts the Flask development server.
#
# debug=True
# Automatically reloads the server after code changes
# and displays detailed error messages.

# ----------------------------------------------------------
# 9. Running the Flask Application
#
# Method 1:
#
# python app.py
#
# Method 2:
#
# flask run

# ----------------------------------------------------------
# 10. Default Flask Server
#
# After running:
#
# http://127.0.0.1:5000/
#
# Open this URL in your browser.

# ----------------------------------------------------------
# 11. Flask Routing
#
# A route maps a URL to a Python function.

@app.route("/about")
def about():
    return "About Page"

# Visiting:
#
# http://127.0.0.1:5000/about

# ----------------------------------------------------------
# 12. Multiple Routes

@app.route("/")
def home():
    return "Home"

@app.route("/contact")
def contact():
    return "Contact Page"

@app.route("/services")
def services():
    return "Services"

# ----------------------------------------------------------
# 13. Dynamic Routes

@app.route("/user/<name>")
def user(name):
    return "Hello " + name

# URL:
#
# /user/Kirti
#
# Output:
#
# Hello Kirti

# ----------------------------------------------------------
# 14. Route with Integer

@app.route("/square/<int:num>")
def square(num):
    return str(num * num)

# URL:
#
# /square/5
#
# Output:
#
# 25

# ----------------------------------------------------------
# 15. Returning HTML

@app.route("/")
def home():
    return "<h1>Welcome</h1>"

# ----------------------------------------------------------
# 16. Templates Folder
#
# Flask automatically searches for HTML files
# inside the templates folder.
#
# Example:
#
# templates/
#     index.html

# ----------------------------------------------------------
# 17. Rendering HTML Pages

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

# ----------------------------------------------------------
# 18. Static Folder
#
# Used for:
#
# - CSS
# - JavaScript
# - Images
# - Fonts
#
# Example:
#
# static/
#     css/
#     js/
#     images/

# ----------------------------------------------------------
# 19. Passing Data to HTML

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Kirti"
    )

# HTML:
#
# <h1>{{ name }}</h1>

# ----------------------------------------------------------
# 20. Debug Mode

app.run(debug=True)

# Advantages:
#
# - Auto reload
# - Detailed error messages

# Disable in production.

# ----------------------------------------------------------
# 21. Project Structure

# FlaskProject/
#
# app.py
#
# templates/
#     index.html
#     about.html
#
# static/
#     css/
#     js/
#     images/
#
# venv/

# ----------------------------------------------------------
# 22. Common Flask Commands
#
# Install Flask:
#
# pip install flask
#
# Create Virtual Environment:
#
# python -m venv venv
#
# Activate:
#
# venv\Scripts\activate
#
# Run:
#
# python app.py
#
# OR
#
# flask run

# ----------------------------------------------------------
# 23. Common Interview Questions
#
# Q1. What is Flask?
#
# Flask is a lightweight Python web framework used
# to build web applications and REST APIs.
#
# ------------------------------------------------
#
# Q2. Why is Flask called a micro-framework?
#
# Because it provides only the essential features,
# allowing developers to add extensions as needed.
#
# ------------------------------------------------
#
# Q3. What is routing?
#
# Routing maps a URL to a Python function.
#
# ------------------------------------------------
#
# Q4. What is the purpose of app = Flask(__name__)?
#
# It creates the Flask application instance.
#
# ------------------------------------------------
#
# Q5. What does @app.route() do?
#
# It associates a URL with a function.
#
# ------------------------------------------------
#
# Q6. Why use debug=True?
#
# It automatically reloads the server after changes
# and provides detailed error information.
#
# ------------------------------------------------
#
# Q7. What is the templates folder used for?
#
# To store HTML files rendered by Flask.
#
# ------------------------------------------------
#
# Q8. What is the static folder used for?
#
# To store CSS, JavaScript, images, and other
# static resources.

# ----------------------------------------------------------
# 24. Quick Revision
#
# Install Flask:
#
# pip install flask
#
# Create Virtual Environment:
#
# python -m venv venv
#
# Activate:
#
# venv\Scripts\activate
#
# Import Flask:
#
# from flask import Flask
#
# Create App:
#
# app = Flask(__name__)
#
# Create Route:
#
# @app.route("/")
#
# Run Server:
#
# app.run(debug=True)
#
# Render HTML:
#
# render_template("index.html")
#
# Templates Folder:
#
# templates/
#
# Static Files:
#
# static/

# ----------------------------------------------------------
# Summary
#
# Flask is a lightweight Python web framework used to
# build websites and APIs. A Flask application starts
# by creating an app object, defining routes with
# @app.route(), and running the server. HTML files are
# stored in the templates folder, while CSS, JavaScript,
# and images are stored in the static folder.