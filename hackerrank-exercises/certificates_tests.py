# def fizzBuzz(n):
#     for i in range(n + 1):
#         if i == 0:
#             pass
#         else:
#             if i % 3 == 0: 
#                 if i % 5 == 0:
#                     print("FizzBuzz")
#                 else:
#                     print("Fizz")
#             elif i % 5 == 0:
#                 print("Buzz")
#             else:
#                 print(i)
    
# fizzBuzz(20)

# import math

# class Rectangle:
# def __init__(self, l, b):
#         self.length = l
#         self.breath = b
    
# def area(self):
#     rec_area = self.length * self.breath
#     return (float(rec_area))



# class Circle:
#     def __init__(self, r):
#         self.radius = r
    
#     def area(self):
#         cir_area = math.pi * (r ** 2)
#         return (float(cir_area))


# class Car:
#     def __init__(self, maxim, units):
#         self.maxim = maxim
#         self.units = units
        
#     def __str__(self):
#         return("Car with the maximum speed of {0} {1}"
#         .format(self.maxim, self.units))


# class Boat:
#     def __init__(self, maxim):
#         self.maxim = maxim
        
#     def __repr__(self):
#         return("Boat with the maximum speed of {0} knots"
#         .format(self.maxim))


# def filledOrders(order, k):
#     max_order = 0
#     for i in order:
#         if i <= k:
#             max_order += 1
#             k -= i
#     return max_order

def findSubstring(s, k):
    vowels = "aeiou" 
    counts = 0
    while counts < 5:   
        vowel = vowels[counts] 
        vowel_count = 0
        for index, item in enumerate(s):    
            if item == vowel:
                vowel_count += 1
                if vowel_count == 2:  
                    print(s[index - k:index + 1])                  
                    return s[index - k:index + 1]
        counts += 1   

findSubstring("azerdii", 5)