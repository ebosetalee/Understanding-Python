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


# help(webbrowser)
# webbrowser.open("https://www.python.org/")
# webbrowser.open_new_tab("https://docs.python.org/3.8/library/webbrowser")

# webbrowser.get(using None) - provides what you need to use a diff browser to the system's default...

# chrome = webbrowser.get(using="google-chrome")
# chrome.open_new("https://www.python.org/")
# BUT FOR SAFARI, IT WORKS THIS WAY.

# OR for mac:
# chrome = webbrowser.get("google-chrome %s").open("https://www.python.org/")


# In looking at a documentation, note the difference between arguments and parameters:
# but sometimes used interchangeably.