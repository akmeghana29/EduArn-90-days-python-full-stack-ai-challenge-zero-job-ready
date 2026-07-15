# ==========================================================
#                  FLASK ROUTES NOTES
# ==========================================================

# ----------------------------------------------------------
# 1. What is Routing?
#
# Routing is the process of mapping a URL to a Python function.
#
# Whenever a user visits a URL, Flask executes the corresponding
# function and returns a response.
#
# Example:
#
# URL                     Function
# -------------------------------
# /                        home()
# /about                   about()
# /contact                 contact()

# ----------------------------------------------------------
# 2. Basic Route

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask!"

# "/" represents the home page.

# ----------------------------------------------------------
# 3. Multiple Routes

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

@app.route("/services")
def services():
    return "Services Page"

# ----------------------------------------------------------
# 4. How Routing Works
#
# User enters URL
#        ↓
# Flask checks matching route
#        ↓
# Calls corresponding function
#        ↓
# Function returns response
#        ↓
# Browser displays response

# ----------------------------------------------------------
# 5. Dynamic Routes
#
# Dynamic routes allow values to be passed through the URL.

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

# URL:
# /user/Kirti
#
# Output:
# Hello Kirti

# ----------------------------------------------------------
# 6. Multiple Dynamic Parameters

@app.route("/student/<name>/<course>")
def student(name, course):
    return f"{name} studies {course}"

# URL:
# /student/Kirti/CSE
#
# Output:
# Kirti studies CSE

# ----------------------------------------------------------
# 7. Integer Converter

@app.route("/square/<int:number>")
def square(number):
    return str(number * number)

# URL:
# /square/5
#
# Output:
# 25

# ----------------------------------------------------------
# 8. Float Converter

@app.route("/circle/<float:radius>")
def area(radius):
    return str(3.14 * radius * radius)

# URL:
# /circle/4.5

# ----------------------------------------------------------
# 9. Path Converter
#
# Accepts complete path including '/'

@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

# Example:
#
# /files/images/profile/photo.jpg

# ----------------------------------------------------------
# 10. String Converter
#
# Default converter.

@app.route("/city/<string:name>")
def city(name):
    return name

# ----------------------------------------------------------
# 11. URL Converters

# string
# int
# float
# path
# uuid

# ----------------------------------------------------------
# 12. Returning HTML

@app.route("/")
def home():
    return "<h1>Welcome</h1>"

# ----------------------------------------------------------
# 13. Returning Multiple Lines

@app.route("/profile")
def profile():
    return """
    <h1>Profile</h1>
    <p>Welcome User</p>
    """

# ----------------------------------------------------------
# 14. Route Methods
#
# By default, Flask allows only GET requests.

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello"

# ----------------------------------------------------------
# 15. GET Request

@app.route("/login", methods=["GET"])
def login():
    return "Login Page"

# Used for retrieving data.

# ----------------------------------------------------------
# 16. POST Request

@app.route("/submit", methods=["POST"])
def submit():
    return "Form Submitted"

# Used for sending data.

# ----------------------------------------------------------
# 17. Multiple HTTP Methods

@app.route("/register", methods=["GET", "POST"])
def register():
    return "Registration"

# ----------------------------------------------------------
# 18. Route with Variables

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return str(a + b)

# URL:
# /add/10/20
#
# Output:
# 30

# ----------------------------------------------------------
# 19. Redirecting Routes

from flask import redirect

@app.route("/google")
def google():
    return redirect("https://www.google.com")

# ----------------------------------------------------------
# 20. URL Building

from flask import url_for

@app.route("/")
def home():
    return url_for("about")

@app.route("/about")
def about():
    return "About"

# Output:
# /about

# ----------------------------------------------------------
# 21. Route Endpoint
#
# The function name acts as the endpoint.

@app.route("/contact")
def contact():
    return "Contact"

# Endpoint:
# contact

# ----------------------------------------------------------
# 22. Error Handling

@app.route("/error")
def error():
    return "Something went wrong"

# Flask automatically returns:
#
# 404
# if route is not found.

# ----------------------------------------------------------
# 23. Common Route Examples

@app.route("/")
def home():
    return "Home"

@app.route("/about")
def about():
    return "About"

@app.route("/products")
def products():
    return "Products"

@app.route("/contact")
def contact():
    return "Contact"

# ----------------------------------------------------------
# 24. Running the Application

if __name__ == "__main__":
    app.run(debug=True)

# Open Browser:
#
# http://127.0.0.1:5000/

# ----------------------------------------------------------
# 25. Common Interview Questions
#
# Q1. What is routing in Flask?
#
# Routing maps a URL to a Python function.
#
# ------------------------------------------------
#
# Q2. What is @app.route()?
#
# It is a decorator used to associate a URL with a function.
#
# ------------------------------------------------
#
# Q3. What is a dynamic route?
#
# A route that accepts values through the URL.
#
# Example:
# /user/<name>
#
# ------------------------------------------------
#
# Q4. Name the common URL converters.
#
# string
# int
# float
# path
# uuid
#
# ------------------------------------------------
#
# Q5. What is the default HTTP method?
#
# GET
#
# ------------------------------------------------
#
# Q6. Difference between GET and POST?
#
# GET:
# Retrieves data.
#
# POST:
# Sends data to the server.
#
# ------------------------------------------------
#
# Q7. What does url_for() do?
#
# Generates a URL using the function name instead of
# hardcoding the URL.
#
# ------------------------------------------------
#
# Q8. What happens if no matching route exists?
#
# Flask returns a 404 Not Found error.

# ----------------------------------------------------------
# 26. Quick Revision
#
# Create Route:
#
# @app.route("/")
#
# Dynamic Route:
#
# @app.route("/user/<name>")
#
# Integer Route:
#
# @app.route("/square/<int:number>")
#
# Multiple Methods:
#
# methods=["GET", "POST"]
#
# Redirect:
#
# redirect()
#
# Build URL:
#
# url_for()
#
# Start Server:
#
# app.run(debug=True)

# ----------------------------------------------------------
# Summary
#
# Routing is one of Flask's core features. It connects URLs
# with Python functions, enabling the application to respond
# to user requests. Flask supports static routes, dynamic
# routes, URL converters, HTTP methods, redirects, and URL
# generation using url_for().