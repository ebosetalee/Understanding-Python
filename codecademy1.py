def sing_song():
  print(''' \n
  You may say I'm a dreamer
  But I'm not the only one
  I hope some day you'll join us
  And the world will be as one''')
 
# call sing_song() below:
sing_song()

sing_song()


sing_song()

def sesan():
  print("""" \n
  I Love you so much dad
  I Love you so much mum
  I Love you so much bro
  I Love you so much You """)
  
sesan()  

def mult_x_add_y(number, x, y):
  print(number*x + y)
  
mult_x_add_y(1, 3, 1)
  
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+ title +" with "+str(row_count)+" rows.")
  
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

age = calculate_age(2018, 1953)

print("I am " + " years old and my dad is " + str(age) + " years old.")

def divide_by_four(input_number):
  return input_number/4

result = divide_by_four(16)

print(int(result))


def create_special_string(special_item):
  return "Our special is " + special_item + "."

special_string = create_special_string("banana yoghurt")

print(special_string)

def calculate_birthday(current_year, married_year):
  marriage_anniversary = current_year - married_year
 
  return marriage_anniversary
print(calculate_birthday(2018 , 1998))

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2

x_squared, y_squared = square_point(1,3)
print(x_squared)
print(y_squared)

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

print(get_boundaries(100, 20))

current_year = 2048

def calculate_age_2(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age_2(1970))

