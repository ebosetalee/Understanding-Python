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

# print the value for requestId from the JSON output
print()
print("requestId")
print(results[requestId])

# print the value for dominantColorBackground from the color keys
print("dominantColorBackground")
print(results["color"]["dominantColorBackground"])

# print out all the tags in the description
print("all tags")
for item in results["description"]["tags"]:
    print(item)

# print out the first tag in the description
print("first_tag")
print(results["description"]["tags"][0])

# To manage keys, we can use environmental variables. i.e Values from
# outside your application such as connecting to database, determining
# the os; setings which need to change; sensitive data.
# 
# We'll import the os lib and call a function called getenv and then pass
# in the name of this system variable or environmental variable that we want.
#   
import os 
os_version = os.getenv("os")
print(os_version)

# Another is dotenv: it is a package that has a version available for every
# major programming environment. It gives the opportunity to set and store those
# environmental variables inside of a text file. Thus, no hard code and no checking
# of sensitive values into source sontrol.

# .env file - create a .env file
# DATABASE=Sample_Connection_String 
# 
# app.py
# from dotenv import load_dotenv
# import os 
# load_dotenv()
# database = os.getenv("DATABASE") 
# print(database) 