# Error handling is when there's a problem with the code and it's not something we can predict when the code is pushed out to production.
# e.g Permission issues, server being down, database changing etc.
# Debuggin is when there's a problem with the code, thereby giving a wrong answer. 

# NOtE try, except, finally - not used for debugging. 
# Error types: Syntax error; runtime error; Logic errors.

# Catching runtime error: 
try: 
    print(x/y)
except ZeroDivisionError as e:
    # Optionally log e somewhere
    print("Sorry, something went wrong")
except:
    print("Something really went wrong")
finally:
    print("This always runs on success or failure")