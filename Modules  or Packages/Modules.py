print(dir())
print(dir(__builtins__))

import shelve


print(dir())
print(dir(shelve))

for m in dir(shelve):
    print(m)

# help(shelve)

# web browser is the simplest module 
# in the python standard library
# it doesn't implement web browser but
# It allows to launch one of installed browser 
# and navigate to a single url 

import webbrowser


webbrowser.open("https://www.python.org/")
webbrowser.open_new_tab("https://www.python.org/")
