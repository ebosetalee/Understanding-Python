import datetime
# time = datetime.datetime.now()
# print(time) # the computer determines the time and its a 24 hours difference

# spectime = datetime.datetime(2016, 7,22, 20,5,24,574376)
# new_time = datetime.datetime.now()
# str(new_time)
# print(new_time)

# time = new_time - spectime
# print(time)
# print(time.days)
# print(time.total_seconds())


# filename = datetime.datetime.now()

# def create_file():
#   """ This function creates an empty file """
#   with open(str(filename), "w+") as file:
#     file.write("")

# create_file()


import time
empty_list = []
for i in range(5):
  empty_list.append(datetime.datetime.now())
  time.sleep(1) # Note this
print(empty_list)
for i in empty_list:
  print(i)