print("\n")
print ("      << ŽAIDIMAS >> \n X KRYŽIUKAI ir NULIUKAI O")

langelis = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]


def atvaizdavimas_langelyje():
    print("\n")
    print(langelis[0] + " | " + langelis[1] + " | " + langelis[2] + "     1 | 2 | 3")
    print(langelis[3] + " | " + langelis[4] + " | " + langelis[5] + "     4 | 5 | 6")
    print(langelis[6] + " | " + langelis[7] + " | " + langelis[8] + "     7 | 8 | 9")
    print("\n")

zaidimas_dar_vyksta = True

dabartinis_zaidejas = "X"

def zaisti():
    atvaizdavimas_langelyje()

    while zaidimas_dar_vyksta:
        pasrinkimas(dabartinis_zaidejas)
        ieskoti_kada_pabaiga()
        pakeisti_zaideja()

    if nugaletojas == "X" or nugaletojas == "O":
        print(nugaletojas + "\033[32;5m Laimėjo !!!\033[0m", "(ᵔᴥᵔ)")
    elif nugaletojas == None:
        print(" Lygiosios ¯\_(ツ)_/¯")

def pasrinkimas (zaidejas):
    print("Dabar žaidžia " + zaidejas)
    pozicija = input("Rinkis skaičių nuo 1-9: ")

    validus = False
    while not validus:

        while pozicija not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pozicija = input("Rinkis skaičių nuo 1-9: ")

        pozicija = int(pozicija) - 1

        if langelis [pozicija] == "-":
            validus = True
        else:
            print("Ši vieta jau užimta. Rinkis kitą langelį.")

    langelis [pozicija] = zaidejas

    atvaizdavimas_langelyje()

def ieskoti_kada_pabaiga():
    ieskoti_nugaletojo()
    ieskoti_lygiuju()

def ieskoti_nugaletojo():

    global nugaletojas

    eilutes_nugaletojas = ieskoti_eiluteje()
    stulpelio_nugaletojas = ieskoti_stulpelyje()
    istrizaines_nugaletojas = ieskoti_istrizaineje()

    if eilutes_nugaletojas:
        nugaletojas = eilutes_nugaletojas
    elif stulpelio_nugaletojas:
        nugaletojas = stulpelio_nugaletojas
    elif istrizaines_nugaletojas:
        nugaletojas = istrizaines_nugaletojas
    else:
        nugaletojas = None

def ieskoti_eiluteje ():

    global zaidimas_dar_vyksta

    eilute_1 = langelis[0] == langelis[1] == langelis[2] != "-"
    eilute_2 = langelis[3] == langelis[4] == langelis[5] != "-"
    eilute_3 = langelis[6] == langelis[7] == langelis[8] != "-"

    if eilute_1 or eilute_2 or eilute_3:
        zaidimas_dar_vyksta = False

    if eilute_1:
        return langelis[0]
    elif eilute_2:
        return langelis[3]
    elif eilute_3:
        return langelis[6]

    else:
        return None

def ieskoti_stulpelyje():

    global zaidimas_dar_vyksta

    stulpelis_1 = langelis[0] == langelis[3] == langelis[6] != "-"
    stulpelis_2 = langelis[1] == langelis[4] == langelis[7] != "-"
    stulpelis_3 = langelis[2] == langelis[5] == langelis[8] != "-"

    if stulpelis_1 or stulpelis_2 or stulpelis_3:
        zaidimas_dar_vyksta = False

    if stulpelis_1:
        return langelis[0]
    elif stulpelis_2:
        return langelis[1]
    elif stulpelis_3:
        return langelis[2]
    else:
        return None

def ieskoti_istrizaineje():

    global zaidimas_dar_vyksta

    istrizaine_1 = langelis[0] == langelis[4] == langelis[8] != "-"
    istrizaine_2 = langelis[2] == langelis[4] == langelis[6] != "-"

    if istrizaine_1 or istrizaine_2:
        zaidimas_dar_vyksta = False

    if istrizaine_1:
        return langelis[0]
    elif istrizaine_2:
        return langelis[2]

    else:
        return None

def pakeisti_zaideja():

    global dabartinis_zaidejas

    if dabartinis_zaidejas == "X":
        dabartinis_zaidejas = "O"

    elif dabartinis_zaidejas == "O":
        dabartinis_zaidejas = "X"

def ieskoti_lygiuju():

    global zaidimas_dar_vyksta

    if "-" not in langelis:
        zaidimas_dar_vyksta = False
        return True

    else:
        return False

zaisti()
