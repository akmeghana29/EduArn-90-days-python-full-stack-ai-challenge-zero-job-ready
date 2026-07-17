# ==========================================================
#          FLASK REQUEST / RESPONSE CYCLE
# ==========================================================

# ----------------------------------------------------------
# 1. What is the Request-Response Cycle?
#
# The Request-Response Cycle is the process by which a client
# (browser) communicates with a Flask server.
#
# Every time a user visits a webpage, the browser sends an
# HTTP Request to the Flask server.
#
# Flask processes the request and sends back an HTTP Response.
#
# This process repeats for every interaction between the
# client and the server.

# ----------------------------------------------------------
# 2. Components of the Request-Response Cycle
#
# Client (Browser)
#        ↓
# HTTP Request
#        ↓
# Flask Server
#        ↓
# Route Function
#        ↓
# Processing Logic
#        ↓
# HTTP Response
#        ↓
# Browser Displays Result

# ----------------------------------------------------------
# 3. How the Request-Response Cycle Works
#
# Step 1:
# User enters a URL or clicks a link.
#
# Step 2:
# Browser sends an HTTP request.
#
# Step 3:
# Flask receives the request.
#
# Step 4:
# Flask searches for the matching route.
#
# Step 5:
# The corresponding function executes.
#
# Step 6:
# Flask prepares a response.
#
# Step 7:
# Browser receives and displays the response.

# ----------------------------------------------------------
# 4. Example of Request and Response

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask"

if __name__ == "__main__":
    app.run(debug=True)

# Flow:
#
# Browser requests:
# http://127.0.0.1:5000/
#
# Flask executes home()
#
# Flask returns:
# "Welcome to Flask"

# ----------------------------------------------------------
# 5. HTTP Request
#
# A Request is sent from the client to the server.
#
# It contains:
#
# - URL
# - HTTP Method
# - Headers
# - Parameters
# - Cookies
# - Body (optional)

# ----------------------------------------------------------
# 6. HTTP Response
#
# A Response is sent from the server back to the client.
#
# It contains:
#
# - Status Code
# - Headers
# - Response Body
# - Cookies

# ----------------------------------------------------------
# 7. HTTP Methods
#
# GET
# Retrieves data.
#
# POST
# Sends data.
#
# PUT
# Updates data.
#
# DELETE
# Deletes data.
#
# PATCH
# Partially updates data.

# ----------------------------------------------------------
# 8. GET Request Example

@app.route("/about")
def about():
    return "About Page"

# Browser requests:
#
# GET /about

# ----------------------------------------------------------
# 9. POST Request Example

@app.route("/submit", methods=["POST"])
def submit():
    return "Form Submitted"

# Browser sends:
#
# POST /submit

# ----------------------------------------------------------
# 10. Request Object

from flask import request

@app.route("/login")
def login():

    user = request.args.get("username")

    return user

# URL:
#
# /login?username=Kirti

# Output:
#
# Kirti

# ----------------------------------------------------------
# 11. Reading Form Data

from flask import request

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]

    return name

# ----------------------------------------------------------
# 12. Reading JSON Data

from flask import request

@app.route("/api", methods=["POST"])
def api():

    data = request.get_json()

    return data

# ----------------------------------------------------------
# 13. Returning HTML Response

from flask import render_template

@app.route("/")
def home():

    return render_template("index.html")

# ----------------------------------------------------------
# 14. Returning JSON Response

from flask import jsonify

@app.route("/student")
def student():

    return jsonify({

        "name":"Kirti",

        "age":21

    })

# ----------------------------------------------------------
# 15. Redirect Response

from flask import redirect

@app.route("/google")
def google():

    return redirect("https://www.google.com")

# ----------------------------------------------------------
# 16. Status Codes
#
# 200
# OK
#
# 201
# Created
#
# 400
# Bad Request
#
# 401
# Unauthorized
#
# 403
# Forbidden
#
# 404
# Not Found
#
# 500
# Internal Server Error

# ----------------------------------------------------------
# 17. Response Object

from flask import make_response

@app.route("/")
def home():

    response = make_response("Welcome")

    response.status_code = 200

    return response

# ----------------------------------------------------------
# 18. Cookies

from flask import make_response

@app.route("/")
def home():

    response = make_response("Cookie Added")

    response.set_cookie("username","Kirti")

    return response

# ----------------------------------------------------------
# 19. Request Headers

from flask import request

@app.route("/")
def home():

    return request.headers.get("User-Agent")

# ----------------------------------------------------------
# 20. URL Parameters

from flask import request

@app.route("/search")
def search():

    keyword = request.args.get("q")

    return keyword

# URL:
#
# /search?q=python

# ----------------------------------------------------------
# 21. Request-Response Flow Diagram
#
# User
#   │
#   ▼
# Browser
#   │
#   ▼
# HTTP Request
#   │
#   ▼
# Flask Server
#   │
#   ▼
# Route Function
#   │
#   ▼
# Business Logic
#   │
#   ▼
# HTTP Response
#   │
#   ▼
# Browser Displays Page

# ----------------------------------------------------------
# 22. Common Interview Questions
#
# Q1. What is the Request-Response Cycle?
#
# It is the communication process between a client
# and a server where the client sends a request and
# the server processes it and returns a response.
#
# ------------------------------------------------
#
# Q2. What is an HTTP Request?
#
# A message sent from the client to the server asking
# for a resource or action.
#
# ------------------------------------------------
#
# Q3. What is an HTTP Response?
#
# A message sent from the server containing the result
# of processing the request.
#
# ------------------------------------------------
#
# Q4. What are the common HTTP methods?
#
# GET
# POST
# PUT
# DELETE
# PATCH
#
# ------------------------------------------------
#
# Q5. What is the request object?
#
# It stores information sent by the client, such as
# query parameters, form data, JSON data, and headers.
#
# ------------------------------------------------
#
# Q6. What is jsonify() used for?
#
# It converts Python objects into JSON responses.
#
# ------------------------------------------------
#
# Q7. What is render_template() used for?
#
# It renders an HTML template from the templates folder.
#
# ------------------------------------------------
#
# Q8. What is a status code?
#
# A three-digit HTTP code indicating whether the request
# was successful or if an error occurred.

# ----------------------------------------------------------
# 23. Quick Revision
#
# Client
# Browser
#
# Sends
# HTTP Request
#
# Flask
# Processes Request
#
# Route
# Executes Function
#
# Returns
# HTTP Response
#
# Request Object
# request
#
# HTML Response
# render_template()
#
# JSON Response
# jsonify()
#
# Redirect
# redirect()
#
# Status Codes
# 200
# 404
# 500

# ----------------------------------------------------------
# Summary
#
# In Flask, every interaction follows the Request-Response
# Cycle. The browser sends an HTTP request to the Flask
# server, Flask processes the request using the appropriate
# route function, and then sends back an HTTP response.
# Responses can be HTML pages, JSON data, redirects, or
# custom responses with status codes and headers.