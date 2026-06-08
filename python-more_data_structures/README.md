# Python - More Data Structures: Set, Dictionary

## Description
This project focuses on advanced Python data structures, primarily sets and dictionaries. It covers how to manipulate collections of unique data and key-value pairs efficiently without the use of external libraries.

## Learning Objectives
By the end of this project, you should be able to confidently explain and implement:
* How to use sets and understand unique elements
* How to perform mathematical set operations (union, intersection, difference)
* How to work with dictionaries (key-value pairs)
* Methods to add, update, and delete dictionary elements
* How to safely use the .get() method to avoid lookup crashes
* Iterating over sets and dictionaries cleanly

## Core Concepts

### Set
An unordered collection of unique elements. Useful for removing duplicates and conducting mathematical set math.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
```

### Dictionary
An unordered collection of key-value data structures used for fast, mapped lookups.

```python
person = {"name": "Alaa", "age": 20}
print(person.get("name")) # Safely prints: Alaa
```

## Requirements
* Interpreter: Python 3.8.x or higher
* Operating System: Ubuntu 20.04 LTS
* Style Guide: Code must strictly conform to PEP 8 standards using pycodestyle (version 2.8.*)
* Constraints: No external libraries or modules are allowed unless explicitly authorized per task.

## Usage
Ensure your files are marked as executable before running them:

```bash
chmod +x filename.py
./filename.py
```
