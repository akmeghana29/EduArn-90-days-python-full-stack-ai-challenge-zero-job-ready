# ==========================================================
#                JSON HANDLING IN FLASK NOTES
# ==========================================================

# ----------------------------------------------------------
# 1. What is JSON?
#
# JSON stands for JavaScript Object Notation.
#
# It is a lightweight format used for storing and exchanging
# data between a client and a server.
#
# JSON is the most commonly used data format in REST APIs.

# ----------------------------------------------------------
# 2. Why JSON?
#
# Advantages:
#
# - Lightweight
# - Easy to Read
# - Easy to Write
# - Language Independent
# - Fast Data Exchange
# - Supported by almost all programming languages

# ----------------------------------------------------------
# 3. JSON Syntax
#
# JSON stores data as key-value pairs.
#
# Example:
#
# {
#     "name":"Kirti",
#     "age":21,
#     "course":"CSE"
# }

# ----------------------------------------------------------
# 4. JSON Data Types
#
# String
#
# {
#     "name":"Kirti"
# }
#
# Number
#
# {
#     "age":21
# }
#
# Boolean
#
# {
#     "student":true
# }
#
# Array
#
# {
#     "marks":[90,85,95]
# }
#
# Object
#
# {
#     "address":{
#         "city":"Delhi"
#     }
# }
#
# Null
#
# {
#     "phone":null
# }

# ----------------------------------------------------------
# 5. JSON vs Python Dictionary
#
# JSON
#
# {
#     "name":"Kirti"
# }
#
# Python
#
# {
#     "name":"Kirti"
# }
#
# Difference:
#
# JSON is a text format.
#
# Python Dictionary is a Python object.

# ----------------------------------------------------------
# 6. Python json Module

import json

# Used for converting between Python objects
# and JSON data.

# ----------------------------------------------------------
# 7. Python Object to JSON
#
# json.dumps()

import json

student = {

    "name":"Kirti",

    "age":21
}

json_data = json.dumps(student)

print(json_data)

# Output:
#
# '{"name":"Kirti","age":21}'

# ----------------------------------------------------------
# 8. JSON to Python Object
#
# json.loads()

json_string = '{"name":"Kirti","age":21}'

student = json.loads(json_string)

print(student)

# Output:
#
# {'name':'Kirti','age':21}

# ----------------------------------------------------------
# 9. Writing JSON to a File
#
# json.dump()

student = {

    "name":"Kirti",

    "age":21
}

with open("student.json","w") as file:

    json.dump(student,file,indent=4)

# ----------------------------------------------------------
# 10. Reading JSON from a File
#
# json.load()

with open("student.json","r") as file:

    data = json.load(file)

print(data)

# ----------------------------------------------------------
# 11. JSON in Flask
#
# Flask commonly uses JSON for communication
# between client and server.

# ----------------------------------------------------------
# 12. Returning JSON Response

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/student")
def student():

    return jsonify({

        "name":"Kirti",

        "age":21,

        "course":"CSE"

    })

# jsonify() converts a Python dictionary
# into a JSON response.

# ----------------------------------------------------------
# 13. Returning a List

@app.route("/students")
def students():

    return jsonify([

        {

            "id":1,

            "name":"Kirti"

        },

        {

            "id":2,

            "name":"Rahul"

        }

    ])

# ----------------------------------------------------------
# 14. Receiving JSON Data

from flask import request

@app.route("/student", methods=["POST"])
def add_student():

    data = request.get_json()

    return jsonify(data)

# ----------------------------------------------------------
# 15. Accessing JSON Values

@app.route("/student", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data["name"]

    age = data["age"]

    return jsonify({

        "name":name,

        "age":age

    })

# ----------------------------------------------------------
# 16. Sample JSON Request
#
# POST /student
#
# {
#     "name":"Kirti",
#     "age":21
# }

# ----------------------------------------------------------
# 17. Sample JSON Response
#
# {
#     "name":"Kirti",
#     "age":21
# }

# ----------------------------------------------------------
# 18. jsonify() vs json.dumps()
#
# jsonify()
#
# Used inside Flask.
#
# Returns an HTTP JSON response.
#
# -------------------------------
#
# json.dumps()
#
# Converts a Python object into a JSON string.
#
# Does NOT create an HTTP response.

# ----------------------------------------------------------
# 19. request.get_json()
#
# Reads JSON data sent by the client.

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data["username"]

    password = data["password"]

    return jsonify({

        "message":"Login Successful"

    })

# ----------------------------------------------------------
# 20. JSON Response with Status Code

@app.route("/student")
def student():

    return jsonify({

        "message":"Success"

    }), 200

# ----------------------------------------------------------
# 21. Nested JSON

student = {

    "name":"Kirti",

    "address":{

        "city":"Delhi",

        "country":"India"

    }

}

# ----------------------------------------------------------
# 22. JSON Array

students = [

    {

        "id":1,

        "name":"Kirti"

    },

    {

        "id":2,

        "name":"Rahul"

    }

]

# ----------------------------------------------------------
# 23. Common JSON Functions
#
# json.dumps()
#
# Python Object → JSON String
#
# ------------------------------
#
# json.loads()
#
# JSON String → Python Object
#
# ------------------------------
#
# json.dump()
#
# Write JSON to File
#
# ------------------------------
#
# json.load()
#
# Read JSON from File
#
# ------------------------------
#
# jsonify()
#
# Python Object → Flask JSON Response
#
# ------------------------------
#
# request.get_json()
#
# Read JSON from Request

# ----------------------------------------------------------
# 24. Common Interview Questions
#
# Q1. What is JSON?
#
# JSON is a lightweight format used for storing
# and exchanging data.
#
# ------------------------------------------------
#
# Q2. Why is JSON used in REST APIs?
#
# Because it is lightweight, easy to read,
# language-independent, and widely supported.
#
# ------------------------------------------------
#
# Q3. Difference between JSON and Python Dictionary?
#
# JSON is a text format.
#
# Dictionary is a Python object.
#
# ------------------------------------------------
#
# Q4. Difference between jsonify() and json.dumps()?
#
# jsonify()
# Returns a Flask HTTP response.
#
# json.dumps()
# Returns a JSON string.
#
# ------------------------------------------------
#
# Q5. Which Flask function reads JSON data?
#
# request.get_json()
#
# ------------------------------------------------
#
# Q6. Which Flask function sends JSON data?
#
# jsonify()
#
# ------------------------------------------------
#
# Q7. Difference between dump() and dumps()?
#
# dump()
# Writes JSON to a file.
#
# dumps()
# Converts a Python object into a JSON string.

# ----------------------------------------------------------
# 25. Quick Revision
#
# JSON
#
# Data Exchange Format
#
# Python → JSON
#
# json.dumps()
#
# JSON → Python
#
# json.loads()
#
# Write File
#
# json.dump()
#
# Read File
#
# json.load()
#
# Flask Response
#
# jsonify()
#
# Read Request
#
# request.get_json()

# ----------------------------------------------------------
# Summary
#
# JSON is the standard format for exchanging data in REST
# APIs. Flask provides jsonify() to send JSON responses and
# request.get_json() to receive JSON requests. Python's json
# module supports converting between Python objects and JSON
# strings, as well as reading from and writing to JSON files.
