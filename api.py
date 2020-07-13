# How to call an API
# A web service is when a developer wants to share the functionality but not the actual code in the program, they can place the function on a web server.
# A programmer with the address of that function on the web server and the required permissions can call the function. e.g documentation.
# API - Application Programming Interface: The messanger that takes requests, tells the system what you want it to do; then
# returns the response back to you e.g waiter. In other words, it is part of the server that receoves request and send responses.
# You can't call a function unless you know the function name and the required parameters
# When you create a web service you create an Application Programming Interface (API)
# 
# The API defines the functon names and parameters so others know how to call your function.
# 
# Keys allow me to track which users have permission to use my web service.
# A developer signs up on my web site, or buys a license for m software and is provided a unique key.
# 
# When the developer calls my web service they provide their unique key and i am able to verify the key has been approved for calls to my web service 
# A standard way of sending messages across the web is the HTTP - Hypertext Transfer Protocol.
# There are two standard protocols for sending messages under HTTP - a. Get and b. Post. The documentation will tell you which to use.
# Get command you pass value to the function using query string, special characters (slash\) must be escaped and limited amount of data that can be passed in
# Post command can pass values with query string and message body, no need to escape and more data 

# The "requests library" simplifies HTTP calls from Python code, because it simplifies making a POST or GET call. Thus,
# Import the request library, pip install first, then you can call requests.post 
# 
# DOCUMENTATION IS KEY!!
# To escape special characters you use \"" if useing double quotes for strings or \'' for single quote or """ """


# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
import requests

# We will need the json library to read the data passed back 
# by the web service
import json

# You need to update the SUBSCRIPTION_KEY to 
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

# Add the name of the function you want to call to the address
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))