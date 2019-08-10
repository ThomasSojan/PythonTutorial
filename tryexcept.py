try:
    age = int(input("enter age : "))
    salary = 20000
    risk = salary/age
    print(f'age = {age} salary = {salary} risk = {risk}')
except ValueError :
    print("Invalid value")
except ZeroDivisionError:
    print("age cannot be zero")    
     




