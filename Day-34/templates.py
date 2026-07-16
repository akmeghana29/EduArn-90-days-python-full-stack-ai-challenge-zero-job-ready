# ==========================================================
#              FLASK TEMPLATES (JINJA2) NOTES
# ==========================================================

# ----------------------------------------------------------
# 1. What are Templates?
#
# Templates are HTML files that Flask renders and sends
# to the browser.
#
# Instead of writing HTML inside Python code, Flask stores
# HTML files inside a "templates" folder.
#
# Flask uses the Jinja2 template engine to create dynamic
# HTML pages.

# ----------------------------------------------------------
# 2. What is Jinja2?
#
# Jinja2 is Flask's default template engine.
#
# It allows us to:
# - Display Python variables
# - Use loops
# - Use conditions
# - Reuse HTML layouts
# - Create dynamic web pages

# ----------------------------------------------------------
# 3. Project Structure
#
# FlaskProject/
#
# app.py
#
# templates/
#     index.html
#     about.html
#     contact.html
#
# static/
#     css/
#     js/
#     images/

# ----------------------------------------------------------
# 4. render_template()
#
# Flask uses render_template() to render HTML files.
#
# Example:

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Flask automatically searches inside the templates folder.

# ----------------------------------------------------------
# 5. index.html
#
# templates/index.html
#
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Home</title>
# </head>
# <body>
#     <h1>Welcome</h1>
# </body>
# </html>

# ----------------------------------------------------------
# 6. Passing Variables to Templates

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Kirti"
    )

# HTML

# <h1>Hello {{ name }}</h1>

# Output:
#
# Hello Kirti

# ----------------------------------------------------------
# 7. Passing Multiple Variables

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Kirti",
        age=21,
        course="CSE"
    )

# HTML

# Name: {{ name }}
#
# Age: {{ age }}
#
# Course: {{ course }}

# ----------------------------------------------------------
# 8. Jinja2 Syntax

# Display Variable

# {{ variable }}

# Example

# {{ name }}

# ----------------------------------------------------------
# 9. Jinja2 Comments

# {# This is a comment #}

# Not displayed in browser.

# ----------------------------------------------------------
# 10. if Statement

# HTML

# {% if marks >= 40 %}
#
#     Pass
#
# {% else %}
#
#     Fail
#
# {% endif %}

# ----------------------------------------------------------
# 11. for Loop

# HTML

# <ul>
#
# {% for fruit in fruits %}
#
# <li>{{ fruit }}</li>
#
# {% endfor %}
#
# </ul>

# ----------------------------------------------------------
# 12. Passing Lists

@app.route("/")
def home():

    fruits = ["Apple","Mango","Orange"]

    return render_template(
        "index.html",
        fruits=fruits
    )

# HTML

# {% for fruit in fruits %}
#
# {{ fruit }}
#
# {% endfor %}

# ----------------------------------------------------------
# 13. Passing Dictionaries

@app.route("/")
def home():

    student = {

        "name":"Kirti",

        "age":21
    }

    return render_template(
        "index.html",
        student=student
    )

# HTML

# {{ student.name }}
#
# {{ student.age }}

# ----------------------------------------------------------
# 14. Filters
#
# Filters modify the output.

# Uppercase

# {{ name|upper }}

# Lowercase

# {{ name|lower }}

# Length

# {{ fruits|length }}

# Title Case

# {{ name|title }}

# ----------------------------------------------------------
# 15. Template Inheritance
#
# Allows multiple pages to share the same layout.

# Base Template

# base.html

# <!DOCTYPE html>
# <html>
# <body>
#
# {% block content %}
#
# {% endblock %}
#
# </body>
# </html>

# ----------------------------------------------------------
# 16. Extending Base Template

# index.html

# {% extends "base.html" %}
#
# {% block content %}
#
# <h1>Home Page</h1>
#
# {% endblock %}

# ----------------------------------------------------------
# 17. Including Templates

# Example

# {% include "navbar.html" %}

# Used for:
#
# Navbar
#
# Footer
#
# Sidebar

# ----------------------------------------------------------
# 18. url_for() inside HTML

# HTML

# <a href="{{ url_for('about') }}">
# About
# </a>

# Flask

@app.route("/about")
def about():
    return "About"

# ----------------------------------------------------------
# 19. Static Files

# CSS

# <link rel="stylesheet"
# href="{{ url_for('static',
# filename='css/style.css') }}">

# JavaScript

# <script src="{{ url_for('static',
# filename='js/script.js') }}"></script>

# Image

# <img src="{{ url_for('static',
# filename='images/logo.png') }}">

# ----------------------------------------------------------
# 20. Escaping HTML

@app.route("/")
def home():

    text = "<h1>Hello</h1>"

    return render_template(
        "index.html",
        text=text
    )

# HTML

# {{ text }}

# HTML tags are escaped automatically.

# ----------------------------------------------------------
# 21. Safe Filter

# {{ text|safe }}

# Displays HTML without escaping.

# Use carefully.

# ----------------------------------------------------------
# 22. Common Interview Questions
#
# Q1. What are templates in Flask?
#
# HTML files rendered by Flask using Jinja2.
#
# ------------------------------------------------
#
# Q2. What is Jinja2?
#
# Flask's template engine used to generate dynamic HTML.
#
# ------------------------------------------------
#
# Q3. What does render_template() do?
#
# Loads and renders an HTML file from the templates folder.
#
# ------------------------------------------------
#
# Q4. How do you display a variable in Jinja2?
#
# {{ variable }}
#
# ------------------------------------------------
#
# Q5. How do you write an if statement?
#
# {% if condition %}
#
# {% endif %}
#
# ------------------------------------------------
#
# Q6. How do you write a for loop?
#
# {% for item in list %}
#
# {% endfor %}
#
# ------------------------------------------------
#
# Q7. What is template inheritance?
#
# It allows multiple pages to reuse a common layout.
#
# ------------------------------------------------
#
# Q8. Why use url_for() in templates?
#
# To generate URLs dynamically instead of hardcoding them.

# ----------------------------------------------------------
# 23. Quick Revision
#
# Render Template
#
# render_template("index.html")
#
# Variable
#
# {{ name }}
#
# If Statement
#
# {% if %}
#
# {% endif %}
#
# Loop
#
# {% for %}
#
# {% endfor %}
#
# Comment
#
# {# comment #}
#
# Base Template
#
# {% extends %}
#
# Block
#
# {% block content %}
#
# Include
#
# {% include %}
#
# URL
#
# {{ url_for() }}
#
# Filters
#
# upper
# lower
# title
# length
# safe

# ----------------------------------------------------------
# Summary
#
# Flask uses the Jinja2 template engine to render dynamic
# HTML pages. Templates are stored in the templates folder
# and rendered using render_template(). Jinja2 supports
# variables, loops, conditions, filters, template
# inheritance, and reusable components like headers
# and footers, making web applications more dynamic and
# maintainable.