# 6. Write a Python program to convert a tuple to a string.


def zamiana (krotka):
    str = ' '
    for i in krotka:
        str = str + i
    return str

tuple = ('a', 'b', 'c', 'd', 'e')
str = zamiana (tuple)

print (str)
