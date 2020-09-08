def Hello( name = "everybody"):
    """Greets a person"""
    print("Hello " + name + "!") 
Hello("Peter")
Hello()

def sumsub(a, b, c=0, d=0):
    return (a - b) * (c + d)
print(sumsub(12 , 4))
print(sumsub(42, 15, c = 2))

def hello():
    print("Hello, World")
hello()

Hello()

# def names():
#     name = str(input("Emter your name : "))
#     if set("aeiou").intersection(name.lower()):
#         print("Your name contains a vowel.")
#     else:
#         print("Your name doesn't contain a vowel.")
#     for letter in name:
#         print(letter)
# names()

# def add_numbers(x, y, z):
#     a = x + y
#     b = x + z
#     c = y + z
#     print(a)
#     print(b)
#     print(c)
# add_numbers(1, 2, 3)

def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))
profile_info("Cameron-catfish", 820)
profile_info(followers = 5560, username = "Stanley")

def square(x):
    y = x **2
    return y
result = square(3)
# without return function it prints "none"
print(result)

def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    return a, b, c
sums = add_numbers(1, 2, 3)
print(sums)

def add(num1, num2):
    return num1 + num2

# an example with no return
def no_return(num1, num2):
  num3 = num1 + num2
  return num3
print(add(1, 2))
print(no_return(1, 2))

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

x_squared, y_squared = square_point(1,3)
print(x_squared)
print(y_squared)