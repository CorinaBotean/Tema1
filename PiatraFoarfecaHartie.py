hartie = 1
piatra = 2
foarfeca = 3

def castigator(player1, player2):
    if player1 == player2:
        return 0
    if (player1, player2) in [(hartie, piatra), (foarfeca, hartie), (piatra, foarfeca)]:
        return 1
    else:
        return 2

def alegere(Jucator):
    choice = input(f"{Jucator} Alege: Hartie - 1, Piatra - 2, Foarfeca - 3 ---> ")
    return int(choice)

def main():
    num_runde = int(input("Numărul de runde: "))
    punctaj_player1 = 0
    punctaj_player2 = 0

    for runda in range(1, num_runde + 1):
        print(f"Runda {runda}:")
        player1 = alegere("Jucator 1:")
        player2 = alegere("Jucator 2:")
        rezultat_runda = castigator(player1, player2)

        if rezultat_runda == 1:
            punctaj_player1 += 1
            print("Jucator 1 câștigă runda.")
        elif rezultat_runda == 2:
            punctaj_player2 += 1
            print("Jucator 2 câștigă runda.")
        else:
            print("Egal în runda asta.")

    if punctaj_player1 > punctaj_player2:
        print("Jucator 1 câștigă meciul!")
    elif punctaj_player2 > punctaj_player1:
        print("Jucator 2 câștigă meciul!")
    else:
        print("Meciul se încheie cu un rezultat de egalitate.")

if __name__ == "__main__":
    main()