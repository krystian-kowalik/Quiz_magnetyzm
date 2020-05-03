import os
import random
import time


def clear():
    os.system( 'cls' )


def quiz(pytania, dziedzina):
    start = ""
    while start != "start":
        clear()
        print("Test", dziedzina, "jednokrotnego wyboru\n"
                                 "Wpisz start, aby zacząć: ")
        start = input()
    clear()

    bledy = 0
    wynik = 0
    while bledy != 3:
        clear()
        i = random.randrange(len(pytania))
        pytanie = pytania[i]
        print(pytanie[0], "\n", "a) ", pytanie[1], "\t\tb) ", pytanie[2], "\nc) ", pytanie[3], "\t\td) ", pytanie[4], "\n", sep="")
        odp = input("Odpowiedź: ")
        a = list(odp)
        if pytanie[5] == a[0]:
            print("Dobrze!")
            wynik += 1
        else:
            print("Źle!")
            bledy += 1
        time.sleep(1)

    clear()
    print("Koniec gry!\nTwój wynik:", wynik)
    time.sleep(3)


def zaladuj_pytania(tytul):
    magnetyzm = []

    f = open("magnetyzm.txt", "r") #wczytywanie pliku
    i = 0 #indeks do numerowania linijek
    pytanie = [] #pusta tablica na jedno pytanie z odpowiedziami
    for x in f: #pętla przejeżdżająca plik po kolei linijkami (x to kolejna linijka - string)
        pytanie.append(x.split("\n")[0]) #załączamy kolejne linijki do pytania w formie [pytanie, a, b, c, d, odp]
        if i%6 == 5: #dochodzimy do ostatniego elementu pytania (odp), dodajemy kompletne pytanie i czyścimy na kolejne 5 linijek
            magnetyzm.append(pytanie)
            pytanie = []
        i+=1 #numerowanie linijek
    return magnetyzm #zwrot gotowej tabeli


magnetyzm = zaladuj_pytania("magnetyzm")
quiz(magnetyzm, "magnetyzm")

