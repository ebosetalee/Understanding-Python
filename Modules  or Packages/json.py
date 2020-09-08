import json
# with open("/Users/ella/Documents/DATA.json") as f:
#   data = json.load(f)
#   print(data)
# help(json.load)

# check the https://github.com/ebosetalee/c9-python-getting-started/tree/master/python-for-beginners/17%20-%20JSON
# JSON - JavaScript Object Notation
# Json is a standard data format used to pass data back and forth.
# T o read Json, there's a bunch of websites called JSON linters. 
# The linting tool formats JSON, making it easier to read.
# 
# How to write code that reads JSON:
# JSON contains key pairs- 
# a.) "key":"value"
# b.) "key":{"subkey0":"subvalue0","subkey1":"subvalue1",...} a series of subkeys and subvalues
# c.) {"key":[listvalue), listvalue1, listvalue2, ...]} a list of values to a key.
# Thus, we have to know which structure we're dealing with. 
# There are different methods to read through JSON depending on the value.

# To retrieve from A. i.e "key":"value":
# we import the JSON library like above; then we can retrieve it e.g #print(results["requestId"])
# 
# To retrieve from b i.e subkeys:
# print(results["color"]["dominantColorBackground"])
# 
# To retrieve from c i.e values in a list:
# using index print(results["description"]["tags"][0]) OR
# To get all the tags at once, use a loop-
# for item in results["description"][tags]:
#       print(item)
# 
# To read JSON, you may need to create JSON to pass to a webservice.
# Dictionary is used to create JSON e.g creating "key":"value" JSON onjects from a dictionary.

# create a dictionary object
person_dict = {"first": "Christopher", "last": "Harrison"}
# Add additional key pairs as needed to dictionary
person_dict["city"]="Seattle"

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)
print("-" * 40)

# To create series of subkey and subvalue, we need a nested dictionaries:

# create staff dictionary which assigns a person to a role
staff_dict ={}
staff_dict["Program Manager"] = person_dict

# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)
print("-" * 40)

# To create the list values, we need to add lists to the dictionary.
person_dicts = {"first": "Christopher", "last": "Harrison"}

# Create a list object of programming languages
languages_list = ["Csharp", "Python", "JavaScript"]

# Add list to dictionary
person_dicts["languages"] = languages_list

# Convert dictionary to JSON object
person_jsons = json.dumps(person_dicts)
print(person_jsons)

# When creating and reading JSON
# Use print statements to help debug
# Use a JSON linting tool to make the JSON easier to read
# Have a print out of the full JSON, to figure out the structure when reading specific elements.