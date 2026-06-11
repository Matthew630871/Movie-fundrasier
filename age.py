def check_age(age):
    # This checks that Users inputed data is valid.
    # Age should be higher than 12, and lower than 114.
    if isinstance(age, str):
        return "Please enter an integer (ie: a number which does not haave a decimal part)."
    elif isinstance(age, float):
        return "Please enter an integer (ie: a number which does not haave a decimal part)."
    elif age < 12:
        return "please enter an integer that is more than (or equal to) 12"
    elif age > 114:
        return "Please enter an integer that is less than 115"
    return "thank you"

age = int(input("What is your age? "))  
print(check_age(age))
