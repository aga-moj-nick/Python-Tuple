# 16. Write a Python program to convert a tuple to a dictionary.



def zamiana (krotka, słownik):
    for a, b in krotka:
        słownik.setdefault(a, []).append(b)
    return słownik


krotka = [('Tola', 10), ('Bolek', 5), ('Lolek', 3)]
słownik = {}
print (zamiana (krotka, słownik))
