#args   -   allows to pass multipl non-key arguments
#kwargs - allows u to pass multiple keyword arguments
#         unpacking operator

def add(*args):  #args - tupples
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,3,5))   

def address(**kwargs):  #kwargs - dictionary
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print(address(street="1", city="Isb", state="Pak"))