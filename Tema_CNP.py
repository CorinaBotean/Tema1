def validate_cnp(cnp):
    # Verificăm dacă CNP-ul are lungimea corectă
    if len(cnp) != 13:
        return False

    # Extragem componentele CNP-ului
    sex = int(cnp[0])
    aa = int(cnp[1:3])
    ll = int(cnp[3:5])
    zz = int(cnp[5:7])
    jj = int(cnp[7:9])
    nnn = int(cnp[9:12])
    c = int(cnp[12])

    # Verificăm sexul și secolul
    if sex not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
    if sex == 7 or sex == 8 or sex == 9:
        aa += 1900
    else:
        aa += 2000

    # Verificăm anul de naștere
    if aa < 1800 or aa > 2099:
        return False

    # Verificăm luna și ziua
    if ll < 1 or ll > 12:
        return False
    if zz < 1 or zz > 31:
        return False
    if ll in [4, 6, 9, 11] and zz > 30:
        return False
    if ll == 2:
        if (aa % 4 == 0 and zz > 29) or (aa % 4 != 0 and zz > 28):
            return False

    # Verificăm codul județului
    if jj < 1 or (jj > 46 and (jj < 51 or jj > 52)):
        return False

    # Verificăm cifra de control
    coeficienti = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = sum(int(cnp[i]) * coeficienti[i] for i in range(12))
    rest = suma % 11
    cifra_control = 1 if rest == 10 else rest

    if cifra_control != c:
        return False

    return True


# Exemple de CNP-uri valide și invalide
cnp_valid = "6230902018455"
cnp_invalid = "2930501234567"

if validate_cnp(cnp_valid):
    print(f"{cnp_valid} este un CNP valid.")
else:
    print(f"{cnp_valid} nu este un CNP valid.")

if validate_cnp(cnp_invalid):
    print(f"{cnp_invalid} este un CNP valid.")
else:
    print(f"{cnp_invalid} nu este un CNP valid.")