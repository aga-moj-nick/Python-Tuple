# 17. Write a Python program to unzip a list of tuples into individual lists


lista_krotek = [(1, 2, 3), (4, 5, 6)]

map(list, zip(*lista_krotek))          
print ([list(t) for t in zip(*lista_krotek)])
