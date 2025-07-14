# -*- coding: utf-8 -*-
"""Python Wizard Exercise

A wizard has two magic sets called SetA and SetB. Each of these sets contains a number of different numbers.
The wizard must do two things:

SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}
The wizard must identify all the members in both sets (community).
He must find the common set (share) between SetA and SetB.
Your task is to write a program that:

Find the union of the members in both sets (community) and denote it by u.
Find the common set (share) between SetA and SetB and denote it by i.
The output displays case 1 and 2 respectively on 2 lines and as follows.
{community}
{share}
"""

# define sets
SetA = {1, 2, 3, 4}
SetB = {3, 4, 5, 6}

# calculate unions
u = SetA | SetB  # یا SetA.union(SetB)

# calculate intersection
i = SetA & SetB  # یا SetA.intersection(SetB)

# show output
print(u)
print(i)

