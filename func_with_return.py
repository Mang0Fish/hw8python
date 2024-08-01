def my_avg(a: int = 0, b: int = 0):
    """Returns the average of two integers""" 
    return (a+b)/2 

def my_headline(a :str = "Hello"):
    """Returns the string in uppercase and adds an !"""
    return a.upper()+'!'

def concat_list(a: list[int] = [1], b: list[int] = [2], c: list[int] = [3]):
    '''Returns a combined list out of 3 lists'''
    return a+b+c
    
def string_bool(a: bool = False):
    """Return yes if true, and no otherwise"""
    if a:
        return "yes"
    else:
        return "no"
        
def list_zugi(a: list[int] = [1]):
    """Return whether the number is even or odd"""
    b: list[str] = []
    for i in a:
        if i % 2 == 0:
            b.append("Even")
        else:
            b.append("Odd")
    return b
    
def get_int(a: str = "Enter a number"):
    try:
        num1: int = int(input(a))
        return num1
    except:
        return get_int(a)