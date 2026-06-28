Python - Input/Output

Read, Write, and Serialize Data with Python — Learning file handling and JSON serialization.

Python 3
UTF-8
JSON
Project Overview

This project introduces file handling and JSON serialization in Python. The goal is to learn how to safely read and write text files, append content, and convert Python objects to and from JSON format.

What you will learn

Core skills

Reading UTF-8 text files.

Writing and appending text to files.

Using the with statement for safe file handling.

Serializing Python objects with JSON.

Deserializing JSON back into Python objects.

Working with object dictionaries (__dict__).

Requirements

Python version

Python 3.x

Imports

No external modules unless specified

File encoding

UTF-8

Style

PEP 8 (pycodestyle)

Project Structure
Tasks Summary

Task

	

Description




0. Read file

	

Read a UTF-8 text file and print its content to stdout.




1. Write file

	

Write text to a file and return the number of written characters.




2. Append write

	

Append text to a file without deleting existing content.




3. To JSON string

	

Convert a Python object into a JSON string.




4. From JSON string

	

Convert a JSON string back into a Python object.




5. Save to JSON file

	

Serialize and save an object into a JSON file.




6. Load from JSON file

	

Read a JSON file and deserialize its content.




7. Add item

	

Load a list, append CLI arguments, and save it again.

Example — Task 0 (Read file)

File: 0-read_file.py

Usage:

Key Concepts
Using with
Recommended

The with statement automatically closes files, even if an error occurs.

JSON Serialization

Function

	

Purpose




json.dumps(obj)

	

Object → JSON string




json.loads(s)

	

JSON string → Object




json.dump(obj, file)

	

Object → JSON file




json.load(file)

	

JSON file → Object

How to Run

Make the main script executable (optional):

Run:

Or directly with Python:

Coding Style

Follow PEP 8.

Keep functions short and focused.

Use meaningful variable names.

Prefer with over manual open()/close()
