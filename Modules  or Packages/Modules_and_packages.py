# How to create a module.
# A module is a python file with functions, classes and other componenets.
# It is used to break code down into reuseable structures.
# To create a module, we need to create a file e.g module_message.py

# Either one of these examples does the same but will affect the code in different ways

# 1. import module as namespace
import module_message
module_message.display("Not a warning")

# 2. import all into current namespace
from module_message import * # this * means everything
display("Not a warning")

# 3. import specific items into the current namespace
from module_message import display
display("Not a warning")

# To get a module someone created is called a Package:
# A package is a published collection of modules
# To install them, use pip:

# Install from an individual package
# pip install colorama

# Install from a list of packages
# pip install -r requirements.txt

# requirements.txt
# colorama