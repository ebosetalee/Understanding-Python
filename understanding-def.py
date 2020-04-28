def defaultArg():
  print("Hello World!")

# def userDefFunction(arg1, arg2, arg3 ...):
#     program statement1
#     program statement3
#     program statement3
#     ....
#    return;

# Example:
def defArgFunc(empname, emprole="Manager"):
   print("Emp Name: ", empname)
   print("Emp Role ", emprole)
   return


print("Using default value")
defArgFunc(empname="Nick")
print("************************")
print("Overwriting default value")
defArgFunc(empname="Tom", emprole="CEO")

def addition(a, b, c, d = 16):
  print(a + (b - c) - d)

addition(24, 9, 3, 19)

