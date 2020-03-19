import matplotlib.pyplot as mat
import random as rand
import math
def kartezjusz(k):
    '''Zwraca współrzedne kartezjanskie punktu'''
    wspolrz=[]
    for i in range(0, k):                    #ilosc wymiarow jest rowniez iloscia wspolrzednych punktu
        wspolrz.append(rand.uniform(-1, 1))  #zapisywanie do tabelki liczby niecalkowitej z okreslonego przedzialu
    return wspolrz

assert len(kartezjusz(3))==3,"Funkcja zwraca zla ilosc wspolrzednych"     
assert kartezjusz(0)==[],"Funkcja sie nie wykonala dla 0 wspolrzednych"
    
def promien(tab):
    """Oblicza promien odleglosci"""
    pr=0
    for i in range(0, len(tab)):
        pr+=pow(tab[i], 2)               #podnoszenie do kwadratu
    pr=math.sqrt(pr)                     #pierwiastkowanie sumy kwadratow
    return pr 

assert promien([2, 2, 2, 2])==4, "funkcja promien(tab) nie oblicza promienia"   

if __name__ == "__main__":
    #Testy dzialania funkcji
    wspolrz = []
    print("Dzialanie funkcji losujacej wspolrzedne kartezjanskie: ")
    for i in range(0, 100):
        wspolrz.append(kartezjusz(2))
        print(wspolrz[i])
        if (promien(wspolrz[i]) <= 1):
            mat.plot(wspolrz[i][0], wspolrz[i][1], 'ro')
        else:
            mat.plot(wspolrz[i][0], wspolrz[i][1], 'bo')
    mat.show()
    mat.clf()
