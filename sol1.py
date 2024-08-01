from func_without_return import *
from func_with_return import *

#1
my_ascending(-12, 7)
my_details("AI is the best")
say_bool(True)
say_bool(False)
print_zugi([5, 3, 2, 10, 15, 14, 14])
lstNum1: list[int] =[]
#With bonus
while True:
    num1 = get_int("Enter a grade")
    if num1 == -99:
        break
    else:
        lstNum1.append(num1)
my_statistics(lstNum1)
help(my_ascending)
help(my_details)
help(say_bool)
help(print_zugi)
print(my_statistics)

#2
avg1 = my_avg(99,90)
print(avg1)
head1 = my_headline("Python has conquered the world")
print(head1+' '+head1)
res_con: list[int] = concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(res_con, len(res_con))
help(my_avg)
help(my_headline)
help(concat_list)
print(string_bool(True))
print(list_zugi([1, 3, 4, 2, 6, 8, 7, 9]))

#6
#None, None, break is existing a loop while return is exiting a function