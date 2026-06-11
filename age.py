def check_age(age):
    if isinstance(age, str) or isinstance(age, float):
        return "Please enter an integer (i.e. a number which doesn't have a decimal)."
    elif age < 12:
        return "Please enter an integer that is more than (or equal to) 12."
    elif age > 125:
        return "Please enter an integer that is less than 126."
    
    return "Thank you"