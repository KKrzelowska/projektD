import random as rand
import math
import matplotlib.pyplot as mat
def biegun():
    """Zwraca wspolrzedne biegunowe"""                  
    r=rand.uniform(0, 1)           #punkt znajduje sie wewnatrz okregu o promieniu 1
    fi=rand.uniform(0, 360)        #kat moze wynosic od 0 do 360 
    return r, fi

assert biegun()<(1.1, 361), "Funkcja losuje wartosci spoza przedzialu"
assert biegun()>(-1, -1), "Funkcja losuje wartosci spoza przedzialu"

if __name__ == "__main__":
    #Testy działania funkcji
    print("Dzialanie funkcji losujacej wspolrzedne biegunowe")
    for i in range(0, 100):
        r, fi=biegun()
        x=r*math.cos(fi)
        y=r*math.sin(fi)
        print(r, fi, x, y)
        mat.plot(x, y, 'go')
    mat.show()
    mat.clf()