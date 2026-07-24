# ==========================================================
#              POSTMAN TESTING NOTES
# ========================================================

# ----------------------------------------------------------
# 1. What is Postman?
#
# Postman is an API testing tool used to:
#
# - Send HTTP requests
# - Test REST APIs
# - View API responses
# - Debug APIs
# - Test different HTTP methods
#
# It allows developers to test APIs without creating
# a frontend application.

# ----------------------------------------------------------
# 2. Why Use Postman?
#
# Advantages:
#
# - Easy to use
# - No frontend required
# - Supports all HTTP methods
# - View request and response
# - Test authentication
# - Save API collections
# - Debug APIs quickly

# ----------------------------------------------------------
# 3. Install Postman
#
# Download from:
#
# https://www.postman.com/downloads/
#
# Install and open the application.

# ----------------------------------------------------------
# 4. Starting the Flask Server

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)

# Run:
#
# python app.py
#
# Server URL:
#
# http://127.0.0.1:5000/

# ----------------------------------------------------------
# 5. Making Your First GET Request
#
# Step 1:
# Open Postman.
#
# Step 2:
# Select GET.
#
# Step 3:
# Enter URL:
#
# http://127.0.0.1:5000/
#
# Step 4:
# Click Send.
#
# Response:
#
# Welcome

# ----------------------------------------------------------
# 6. Testing a GET API

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/student")
def student():

    return jsonify({

        "id":1,

        "name":"Kirti",

        "course":"CSE"

    })

# Request:
#
# GET
# http://127.0.0.1:5000/student
#
# Response:
#
# {
#     "id":1,
#     "name":"Kirti",
#     "course":"CSE"
# }

# ----------------------------------------------------------
# 7. Testing a POST API

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/student", methods=["POST"])
def add_student():

    data = request.get_json()

    return jsonify(data)

# ----------------------------------------------------------
# 8. Sending JSON Data
#
# Method:
# POST
#
# URL:
#
# http://127.0.0.1:5000/student
#
# In Postman:
#
# Body
# ↓
# raw
# ↓
# JSON

# Request Body:
#
# {
#     "name":"Kirti",
#     "age":21
# }

# Response:
#
# {
#     "name":"Kirti",
#     "age":21
# }

# ----------------------------------------------------------
# 9. Request Methods Supported
#
# GET
# Retrieve data.
#
# POST
# Create data.
#
# PUT
# Update complete data.
#
# PATCH
# Update partial data.
#
# DELETE
# Delete data.

# ----------------------------------------------------------
# 10. Testing PUT Request

@app.route("/student/<int:id>", methods=["PUT"])
def update_student(id):

    data = request.get_json()

    return jsonify({

        "id":id,

        "updated_data":data

    })

# Method:
#
# PUT
#
# URL:
#
# http://127.0.0.1:5000/student/1

# ----------------------------------------------------------
# 11. Testing PATCH Request

@app.route("/student/<int:id>", methods=["PATCH"])
def patch_student(id):

    data = request.get_json()

    return jsonify({

        "id":id,

        "updated_fields":data

    })

# Method:
#
# PATCH

# ----------------------------------------------------------
# 12. Testing DELETE Request

@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(id):

    return jsonify({

        "message":"Student Deleted",

        "id":id

    })

# Method:
#
# DELETE

# ----------------------------------------------------------
# 13. Query Parameters

from flask import request

@app.route("/search")
def search():

    keyword = request.args.get("q")

    return jsonify({

        "keyword":keyword

    })

# URL:
#
# http://127.0.0.1:5000/search?q=python

# ----------------------------------------------------------
# 14. Path Parameters

@app.route("/student/<int:id>")
def student(id):

    return jsonify({

        "id":id

    })

# URL:
#
# http://127.0.0.1:5000/student/5

# ----------------------------------------------------------
# 15. Headers
#
# Headers provide additional information about the request.
#
# Common Header:
#
# Content-Type : application/json
#
# In Postman:
#
# Headers
# ↓
# Key:
# Content-Type
#
# Value:
# application/json

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
# 17. Response Window
#
# Postman displays:
#
# Response Body
#
# Status Code
#
# Headers
#
# Response Time
#
# Response Size

# ----------------------------------------------------------
# 18. Common Postman Tabs
#
# Params
#
# Authorization
#
# Headers
#
# Body
#
# Scripts
#
# Tests

# ----------------------------------------------------------
# 19. Collection
#
# A Collection is a folder used to organize API requests.
#
# Example:
#
# Student API
#
# ├── GET Students
# ├── POST Student
# ├── PUT Student
# ├── DELETE Student

# ----------------------------------------------------------
# 20. Environment Variables
#
# Instead of writing:
#
# http://127.0.0.1:5000
#
# Create:
#
# base_url
#
# Then use:
#
# {{base_url}}/student

# ----------------------------------------------------------
# 21. Complete Testing Flow
#
# Step 1
#
# Start Flask Server
#
# ↓
#
# Step 2
#
# Open Postman
#
# ↓
#
# Step 3
#
# Select HTTP Method
#
# ↓
#
# Step 4
#
# Enter URL
#
# ↓
#
# Step 5
#
# Add Headers (if needed)
#
# ↓
#
# Step 6
#
# Add Request Body (POST/PUT/PATCH)
#
# ↓
#
# Step 7
#
# Click Send
#
# ↓
#
# Step 8
#
# Check Response

# ----------------------------------------------------------
# 22. Common Interview Questions
#
# Q1. What is Postman?
#
# Postman is an API development and testing tool used
# to send HTTP requests and inspect responses.
#
# ------------------------------------------------
#
# Q2. Why is Postman used?
#
# To test APIs without building a frontend application.
#
# ------------------------------------------------
#
# Q3. Which HTTP methods can Postman send?
#
# GET
# POST
# PUT
# PATCH
# DELETE
#
# ------------------------------------------------
#
# Q4. Why set Content-Type to application/json?
#
# It tells the server that the request body contains
# JSON data.
#
# ------------------------------------------------
#
# Q5. What is a Collection?
#
# A group of saved API requests.
#
# ------------------------------------------------
#
# Q6. What are Environment Variables?
#
# Variables used to store reusable values such as
# base URLs and authentication tokens.

# ----------------------------------------------------------
# 23. Quick Revision
#
# API Testing Tool
#
# Postman
#
# Common Methods
#
# GET
# POST
# PUT
# PATCH
# DELETE
#
# JSON Header
#
# Content-Type: application/json
#
# URL
#
# http://127.0.0.1:5000/
#
# Request Body
#
# Body → raw → JSON
#
# Response
#
# JSON + Status Code
#
# Organize APIs
#
# Collections
#
# Reusable URLs
#
# Environment Variables

# ----------------------------------------------------------
# Summary
#
# Postman is a powerful tool for testing REST APIs. It allows
# developers to send HTTP requests, provide JSON data, inspect
# responses, verify status codes, and debug APIs without
# creating a frontend. It is one of the most commonly used
# tools for backend development and API testing.