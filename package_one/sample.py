"""
sample.py - Sample Module

This is a sample module that demonstrates the structure of a Python module within a package.
When developing a module for your project, you should create a package and some functions like this
to keep your code organized and maintainable.

Package Structure:
    - package_one/
        - __init__.py
        - sample.py

Usage:
    You can import this module within your project's code to use the features it provides.

Example:
    from package_one.sample import f

    result = f(10)

Development Guidelines:
    When creating your own module within a package, follow these guidelines:
    - Create a package directory (e.g., 'package_one') with an '__init__.py' file.
    - Create a Python module (e.g., 'sample.py') within the package directory.
    - Define your classes, functions, and variables within the module.
    - Use an '__init__.py' file to make the package importable.
    - Document your code, including classes, methods, and functions, using docstrings.


    Import and use this module in other parts of your project as needed.

"""


def f(x):
    y = x + 1
    return y
