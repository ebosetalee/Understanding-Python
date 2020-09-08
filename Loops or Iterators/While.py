# this means; 
# while loops repeat as long as a certain boolen condition is met. e.g: 
count = 0
while count <= 6:
    print(count)
    count += 1

statement = "A boy is hungry"
index = 0
while index < len(statement):
    print(statement[index])
    index += 1

for x in statement:
    print(x) 

conuts = 0
#  prints out 0,1,2,3,4
while True:
    print(conuts)
    conuts += 1
    if conuts >= 5:
        break
for x in range(10):
    # prints out only odd numbers -1,3,5,7,9
    # check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Note when using break and continue that in break, the += comes after break 
# but comes before continue as continue skips the print of the condition
