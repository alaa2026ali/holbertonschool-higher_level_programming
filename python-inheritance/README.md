Python - Inheritance
Description

This project introduces the concept of inheritance in Python. Inheritance is one of the fundamental principles of Object-Oriented Programming (OOP). It allows a class to inherit attributes and methods from another class, promoting code reuse and better software design.

Throughout this project, different inheritance concepts are explored, including subclassing, method inheritance, method overriding, and the use of Python built-in functions related to object relationships.

Learning Objectives

At the end of this project, you should be able to explain:

What is a superclass, base class, or parent class
What is a subclass
How to list all attributes and methods of a class or instance
When an instance can have new attributes
How to inherit a class from another
How to define a class with multiple base classes
What is the default class every class inherits from
How to override inherited methods
Which attributes or methods are available through inheritance
The purpose of inheritance
How to use isinstance(), issubclass(), type(), and super()
Requirements
Ubuntu 20.04 LTS
Python 3.8.5
All files must end with a new line
The first line of all Python files must be:
#!/usr/bin/python3
All files must be executable
Code must follow PEP 8 style guidelines (pycodestyle)
All modules, classes, and functions must contain documentation
Project Structure
File	Description
0-lookup.py	Returns the list of available attributes and methods of an object
1-my_list.py	Class that inherits from list and prints a sorted list
2-is_same_class.py	Checks if an object is exactly an instance of a specified class
3-is_kind_of_class.py	Checks if an object is an instance of a class or inherited from it
4-inherits_from.py	Checks if an object is inherited from a specified class
5-base_geometry.py	Empty BaseGeometry class
6-base_geometry.py	BaseGeometry with an area method
7-base_geometry.py	BaseGeometry with integer validation
8-rectangle.py	Rectangle class inheriting from BaseGeometry
9-rectangle.py	Rectangle class with area and string representation
10-square.py	Square class inheriting from Rectangle
11-square.py	Complete Square implementation
Concepts Covered
Inheritance

Inheritance allows a class to reuse the functionality of another class.

Example:

class Animal:
    pass

class Dog(Animal):
    pass
isinstance()

Checks whether an object is an instance of a class or one of its subclasses.

isinstance(obj, MyClass)
issubclass()

Checks whether a class inherits from another class.

issubclass(Dog, Animal)
super()

Allows access to methods from the parent class.

super().__init__()
