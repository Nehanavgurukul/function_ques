# def greet(names): here names parameter is wrong so we'll do right
def greet(*names) :  
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender")