import matplotlib.pyplot as mat
import math
from wspol_kartezjanskie import kartezjusz, promien #dolaczenie funkcji ze stworzonych modulow
from wspol_biegunowe import biegun 
from motywy import motywo

#implementacja modulowa projektu d

if __name__ == '__main__':
    #Podpunkt 1
    k = input("Podaj ilosc wymiarow przestrzeni: ")
    wspolrz = []
    for i in range(0, 1000):                # okreslamy ilosc punktow
        wspolrz.append(kartezjusz(int(k)))  # nadajemy punktom wspolrzedne
        if (int(k) == 2):                   # jesli przestrzen jest dwuwymiarowa program tworzy wykres
            if (promien(wspolrz[i]) <= 1):  # jesli punkt znajduje sie wewnatrz okregu o promieniu 1
                mat.plot(wspolrz[i][0], wspolrz[i][1], 'ro')  # na wykresie otrzyma kolor czerwony
            else:                                             # jesli jest na zewnatrz okregu
                mat.plot(wspolrz[i][0], wspolrz[i][1], 'bo')  # otrzyma kolor niebieski
    mat.savefig('wykres1.png')
    mat.clf()
    # rozklad jest jednostajny jesli prawdopodobienstwo wylosowania kazdego z punktow jest rowne
    # na wykresie widac jednostajnosc rozkladu, punkty wzgledem siebie sa rowno rozlozone

    #Podpunkt 2
    for i in range(0, 1000):    #okreslamy ilosc punktow
        r, fi=biegun()          #losujemy wspolrzedne biegunowe
        x=r*math.cos(fi)        #na podstawie wspolrzednych biegunowych
        y=r*math.sin(fi)        #wyliczamy wspolrzedne kartezjanskie
        mat.plot(x, y, 'ro')    #tworzenie wykresu
    mat.savefig('wykres2.png')  #zapisanie wykresu jako png
    mat.clf()                   #czyszczenie
    #Z wykresu wynika ze rozklad punktow nie jest jednostajny
    #punkty sa gesciej rozlozone blizej srodka ukladu wspolrzednych


    #Podpunkt 3
    profil = [[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7],  # Macierz prawdopodobienstwa pojawienia sie
              [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2],  # nukleotydu na danym miejscu
              [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1],
              [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]
    with open('zestaw_motywow.txt', 'w') as wynik:
        tab = motywo(profil)  # Losowanie zestawu motywow
        for element in tab:
            wynik.write(element)  # zapisywanie do pliku
            wynik.write('\n')
    
