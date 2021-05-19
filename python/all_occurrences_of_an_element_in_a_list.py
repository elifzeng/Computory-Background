# How to find all occurrences of an element in a list
l =[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0]
indices = [i for i, x in enumerate(l) if x == 1]
"""
indices
[7, 9, 13]
"""
