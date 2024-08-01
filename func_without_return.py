def my_ascending(a: int = 0, b: int =0):
    """the function prints the numbers small to big"""
    if a>b:
        print(b, a)
    elif b>a:
        print(a,b)

def my_details(a: str ="hello"):
    """Prints the first, middle, and last character of the string"""
    print(a[0], a[len(a)//2], a[-1])
 
def say_bool(a: bool = False):
    """Prints yes if true, and no otherwise"""
    if a:
        print("yes")
    else:
        print("no")

def print_zugi(a: list[int] = [1]):
    """Print whether thd number in the list is even or odd"""
    for i in a:
        if i%2 == 0:
            print("Even")
        elif i%2 == 1:
            print("Odd")

def my_statistics(a: list[int] = [1]):
    """Prints the highest grade, lowest grade, number of grades and their average
    Bonus: Number of excellent, failed and the standard deviation"""
    if not a:
        a = [1]
    exc: int = 0
    fail: int = 0 
    dev: float = 0
    for i in a:
        if i > 90:
            exc += 1
        elif i < 55:
            fail += 1
    if exc+fail > 0:
        dev = ((100/len(a))*(exc+fail))        
    print(f"Highest {max(a)}, Lowest {min(a)}, Number of grades {len(a)}, Average of grades {sum(a) / len(a)}, Excellent grades {exc}, Failed grades {fail}, Standard deviation {dev}%")