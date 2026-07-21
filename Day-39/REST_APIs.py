# ==========================================================
#                 REST API CONCEPTS NOTES
# ==========================================================

# ----------------------------------------------------------
# 1. What is an API?
#
# API stands for Application Programming Interface.
#
# It is a set of rules that allows two software applications
# to communicate with each other.
#
# Example:
#
# Mobile App  <------API------>  Server
#
# The client sends a request through the API.
# The server processes it and sends back a response.

# ----------------------------------------------------------
# 2. What is REST?
#
# REST stands for Representational State Transfer.
#
# REST is an architectural style used for designing web APIs.
#
# APIs that follow REST principles are called REST APIs.

# ----------------------------------------------------------
# 3. What is a REST API?
#
# A REST API is an API that communicates using HTTP methods
# and exchanges data, usually in JSON format.
#
# Client
#     ↓
# HTTP Request
#     ↓
# REST API
#     ↓
# Database
#     ↓
# HTTP Response (JSON)

# ----------------------------------------------------------
# 4. Why REST APIs?
#
# Advantages:
#
# - Simple
# - Fast
# - Platform Independent
# - Scalable
# - Stateless
# - Easy to Maintain
# - Uses Standard HTTP Methods

# ----------------------------------------------------------
# 5. REST Architecture
#
# Client
#     ↓
# Request
#     ↓
# REST API
#     ↓
# Business Logic
#     ↓
# Database
#     ↓
# Response (JSON)

# ----------------------------------------------------------
# 6. Resources
#
# In REST, everything is treated as a Resource.
#
# Examples:
#
# Student
# Employee
# Product
# User
# Order
#
# Resources are identified using URLs.

# Example:
#
# /students
# /employees
# /products

# ----------------------------------------------------------
# 7. Endpoints
#
# An Endpoint is the URL where an API can be accessed.
#
# Example:
#
# GET /students
#
# POST /students
#
# GET /students/5

# ----------------------------------------------------------
# 8. HTTP Methods
#
# GET
# Retrieve data.
#
# POST
# Create new data.
#
# PUT
# Update an existing resource completely.
#
# PATCH
# Update part of an existing resource.
#
# DELETE
# Delete a resource.

# ----------------------------------------------------------
# 9. CRUD Operations
#
# CRUD stands for:
#
# Create
# Read
# Update
# Delete
#
# Mapping:
#
# Create  -> POST
# Read    -> GET
# Update  -> PUT/PATCH
# Delete  -> DELETE

# ----------------------------------------------------------
# 10. GET Request
#
# Used to retrieve data.
#
# Example:
#
# GET /students
#
# Response:
#
# [
#   {
#       "id":1,
#       "name":"Kirti"
#   }
# ]

# ----------------------------------------------------------
# 11. POST Request
#
# Used to create new data.
#
# Example:
#
# POST /students
#
# Request Body:
#
# {
#   "name":"Kirti",
#   "age":21
# }

# ----------------------------------------------------------
# 12. PUT Request
#
# Updates the entire resource.
#
# Example:
#
# PUT /students/1

# ----------------------------------------------------------
# 13. PATCH Request
#
# Updates only specific fields.
#
# Example:
#
# PATCH /students/1

# ----------------------------------------------------------
# 14. DELETE Request
#
# Deletes a resource.
#
# Example:
#
# DELETE /students/1

# ----------------------------------------------------------
# 15. HTTP Status Codes
#
# 200 OK
#
# Request successful.
#
# 201 Created
#
# Resource successfully created.
#
# 204 No Content
#
# Request successful with no response body.
#
# 400 Bad Request
#
# Invalid request.
#
# 401 Unauthorized
#
# Authentication required.
#
# 403 Forbidden
#
# Access denied.
#
# 404 Not Found
#
# Resource not found.
#
# 500 Internal Server Error
#
# Server error.

# ----------------------------------------------------------
# 16. Request
#
# A Request contains:
#
# URL
#
# HTTP Method
#
# Headers
#
# Body (optional)
#
# Query Parameters

# ----------------------------------------------------------
# 17. Response
#
# A Response contains:
#
# Status Code
#
# Headers
#
# JSON Data

# ----------------------------------------------------------
# 18. JSON
#
# JSON stands for JavaScript Object Notation.
#
# REST APIs usually exchange data in JSON format.
#
# Example:
#
# {
#     "id":1,
#     "name":"Kirti",
#     "course":"CSE"
# }

# ----------------------------------------------------------
# 19. URL Parameters
#
# Example:
#
# GET /students/5
#
# Here,
#
# 5 is the resource ID.

# ----------------------------------------------------------
# 20. Query Parameters
#
# Example:
#
# GET /students?course=CSE
#
# Query Parameter:
#
# course=CSE

# ----------------------------------------------------------
# 21. Headers
#
# Headers provide additional information.
#
# Common Headers:
#
# Content-Type
#
# Authorization
#
# Accept

# ----------------------------------------------------------
# 22. Stateless Nature of REST
#
# REST APIs are Stateless.
#
# This means:
#
# Every request is independent.
#
# The server does not remember previous requests.
#
# Each request must contain all the information needed.

# ----------------------------------------------------------
# 23. REST API Example in Flask

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students")
def students():

    return jsonify([

        {

            "id":1,

            "name":"Kirti"

        }

    ])

if __name__ == "__main__":
    app.run(debug=True)

# ----------------------------------------------------------
# 24. Flask POST Example

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/student", methods=["POST"])
def student():

    data = request.get_json()

    return jsonify(data)

# ----------------------------------------------------------
# 25. REST API Workflow
#
# Client
#      │
#      ▼
# HTTP Request
#      │
#      ▼
# Flask Route
#      │
#      ▼
# Database
#      │
#      ▼
# JSON Response
#      │
#      ▼
# Client

# ----------------------------------------------------------
# 26. REST Principles
#
# 1. Client-Server Architecture
#
# Client and server are independent.
#
# ------------------------------
#
# 2. Stateless
#
# Every request is independent.
#
# ------------------------------
#
# 3. Uniform Interface
#
# Standard URLs and HTTP methods.
#
# ------------------------------
#
# 4. Cacheable
#
# Responses can be cached.
#
# ------------------------------
#
# 5. Layered System
#
# Client doesn't know internal architecture.

# ----------------------------------------------------------
# 27. Common Interview Questions
#
# Q1. What is an API?
#
# A software interface that enables communication
# between applications.
#
# ------------------------------------------------
#
# Q2. What is REST?
#
# An architectural style for designing web services.
#
# ------------------------------------------------
#
# Q3. Difference between REST API and API?
#
# API:
# General communication interface.
#
# REST API:
# API that follows REST principles using HTTP.
#
# ------------------------------------------------
#
# Q4. Difference between PUT and PATCH?
#
# PUT:
# Updates the entire resource.
#
# PATCH:
# Updates only specified fields.
#
# ------------------------------------------------
#
# Q5. Difference between GET and POST?
#
# GET:
# Retrieves data.
#
# POST:
# Creates data.
#
# ------------------------------------------------
#
# Q6. What is JSON?
#
# A lightweight format for exchanging data.
#
# ------------------------------------------------
#
# Q7. Why is REST stateless?
#
# Because the server does not store client state
# between requests.
#
# ------------------------------------------------
#
# Q8. Which Flask function returns JSON?
#
# jsonify()

# ----------------------------------------------------------
# 28. Quick Revision
#
# API
# Communication Interface
#
# REST
# Architectural Style
#
# Resource
# Data Object
#
# Endpoint
# URL
#
# GET
# Read
#
# POST
# Create
#
# PUT
# Update Entire Resource
#
# PATCH
# Partial Update
#
# DELETE
# Delete Resource
#
# JSON
# Data Format
#
# Flask JSON Response
# jsonify()
#
# Read JSON Request
# request.get_json()

# ----------------------------------------------------------
# Summary
#
# REST APIs enable communication between clients and servers
# using standard HTTP methods. Resources are accessed through
# endpoints, data is usually exchanged in JSON format, and
# operations follow CRUD principles. Flask provides support
# for building REST APIs using routes, the request object,
# and jsonify() for returning JSON responses.