#print(my_list)
#print(len(my_list))
#print("Index 4:", my_list[4])
#print("Index 2:", my_list[2])
#print("Index 0:", my_list[0])
#print("Index 4:", my_list[-1])

my_list = [0,1,2,3,4,5,6,7,8,9,10]
print(my_list)
my_sliced_list = my_list[4:]
print(my_sliced_list)
#print(my_list)
#print (len(my_list)) #5

#Tema2 30 August 2023
#declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)
#my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#print(my_list)

#afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă
#my_list.sort()
#print(my_list)

#afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
#my_list.reverse()
#print(my_list)

#afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
#even_numbers = [num for num in my_list if num % 2 == 0]
#even_numbers.sort()
#print(even_numbers)

# afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
#even_numbers = [num for num in my_list if num % 2 !=0]
#even_numbers.sort()
#print(even_numbers)

#afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice)
#even_numbers = [num for num in my_list if num % 3 ==0]
#even_numbers.sort()
#print(even_numbers)

#Top Filme
My_list = [
    {"nume": "George", "filme": ["Shrek", "Bond", "Fight Club"]},
    {"nume": "Cristian", "filme": ["Fight Club", "The Nun", "Dracula", "Bond"]},
    {"nume": "Stefan", "filme": ["Fight Club", "Slumdog Millionaire"]}
]

#Avand o lista de utilizatori si filme vizionate, listati:

#Cel mai vizionat film - Fight Club in cazul de mai sus

#Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus

#Extra
#Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...

#Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan
