# Afisarea meniului
menu = """
1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Stergere lista de cumparaturi
5 - Cautare in lista de cumparaturi
"""

# Citirea opțiunii de la tastatură
try:
    option = int(input("Selectati o optiune (1-5): "))
except ValueError:
    print("Introduceti un numar valid (1-5).")
    exit()

# Verificarea opțiunii și afișarea mesajului corespunzător
if option == 1:
    print("Afisare lista de cumparaturi")
elif option == 2:
    print("Adaugare element")
elif option == 3:
    print("Stergere element")
elif option == 4:
    print("Stergere lista de cumparaturi")
elif option == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")