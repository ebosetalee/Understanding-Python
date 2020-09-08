# Objects, functions and methods.
# Objects are nouns, data constructs - things we create upon.
# Methods are actions and functions are verbs
# Thus os are object, getenv - verb.
# Decorators is like adjectives. They allows us to describe out code. i.e
# Add meaning to codes.
# Decorates are used to add more functionality to code. E.g
# Snippet from Flask
# register https://myserver/api/products

# @route("api/products") - This is the important part.
# def get_products:
#     # code to list from database
#     pass

# Creating a decorator:
def logger(func):
    def wrapper():
        print("Logging execution")
        func()
        print("Done logging")
    return wrapper

@logger # - decorator call
def sample(): # - function
    print("-- Inside sample function")

sample()