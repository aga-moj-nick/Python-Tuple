# 19. Write a Python program to convert a list of tuples into a dictionary. 


def zamiana (lista_krotek, słownik):
    for a, b in lista_krotek:
        słownik.setdefault(a, []).append(b)
    return słownik


lista_krotek = [('a', 1), ('b', 2), ('c', 3)]
słownik = {}

print (zamiana (lista_krotek, słownik))
