# -*- coding: utf-8 -*-
"""List Manipulation Exercise
Write code that uses list operators (such as delete and append) to remove the number 3 from the given list 
and append the number 10 to the end of the list, then return the final list.

my_list = [1, 2, 3, 4, 5]
"""

my_list = [1, 2, 3, 4, 5]

my_list.remove(3)

my_list.append(10)

print(my_list)

#If you want to use a function
def modify_list(lst):
    lst.remove(3)
    lst.append(10)
    return lst

my_list = [1, 2, 3, 4, 5]
result = modify_list(my_list)
print(result)
