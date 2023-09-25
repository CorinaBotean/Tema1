def gaseste_al_doilea_minim(lista):
    if len(lista) < 2:
        return "Lista nu are suficiente elemente."

    lista_unica = list(set(lista))  # Elimină duplicatii pentru a evita erori
    lista_unica.sort()  # Sortează lista unică în ordine crescătoare

    if len(lista_unica) < 2:
        return "Nu există al doilea cel mai mic număr."

    return lista_unica[1]

# Exemple
list_1 = [-8, 1, 2, -2, 0]
list_2 = [1, 1, 0, 0, 2, -2, -2]
list_3 = [1, -1, 0, -9, 4, -5]
list_4 = [1, 4, 0, 23, 6, 34]

print("list_1:", gaseste_al_doilea_minim(list_1))
print("list_2:", gaseste_al_doilea_minim(list_2))
print("list_3:", gaseste_al_doilea_minim(list_3))
print("list_4:", gaseste_al_doilea_minim(list_4))

#Lista cu numere de la 1 la n
lista_var = ['p', 's']
n = 5
result = [elem + str(i) for i in range(1, n + 1) for elem in lista_var]
print(result)

#Split dupa al n-lea element dintr-o lista
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [lista_start[i::n] for i in range(n)]
print(result)

# Sortare lista de dictionare folosind functia Lambda
models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]

# Sortați lista de dicționare în funcție de cheia 'model' folosind o funcție lambda
sorted_models = sorted(models, key=lambda x: int(x['model']))

# Afișați lista sortată
for model in sorted_models:
    print(model)

