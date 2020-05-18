# NOTE: continue is used to bypass a certain thing. eg:
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue
    print("Buy " + item)

meal = ["egg "]

# note CAMOCASE = nastyFoodItem