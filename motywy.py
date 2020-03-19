import random as rand
def prawdo(tab):
    """"Losuje nukleotyd korzystajac z dystrybuanty"""
    zasady=['A', 'C', 'G', 'T']
    p=rand.random()                     #losuje liczbe
    if(p<=tab[0]):                      #jesli wylosowana liczba jest w przedziale od 0 do prawdo adeniny
        return zasady[0]                #funkcja zwraca nukleotyd     
    d=tab[0]                            #tworzenie zmiennej o wartosci prawdopodobienstwa wyl. adeniny
    if(p>d and p<=(d+tab[1])):          #jesli wylosowana liczba jest w przedziale od poprzedniej wartosci do sumy wartosci prawdopodobienstw)
        return zasady[1]                #zwraca nukleotyd
    d+=tab[1]
    if(p>d and p<=(d+tab[2])):
        return zasady[2]
    d+=tab[2]
    if(p>d and p<=(d+tab[3])):
        return zasady[3]
    
assert prawdo([0,0, 0, 1])=='T', "Funkcja nie losuje wg rozkladu prawdopodobientwa"
assert prawdo([0,0,0,0])==None,"Problemy z funkcja przy podaniu sumy prawdopodobienstw 0"

def motywo(profil):
    """Losuje zestawy nukleotydow, o czestosci okreslonej przez macierz"""
    motyw=''
    zestaw_motywow=[]
    for j in range(0, 1000):                     #okreslenie ilosci motywow
        for i in range(0, len(profil[0])):       #iterowanie po 8 elementach
            tab = []
            for x in range(0, len(profil)):                #tworzenie tabelki prawdopodobienstw dla kazdego nukleotydu na danym miejscu
                tab.append(profil[x][i])
            motyw += str(prawdo(tab))                   #dodawanie nukleotydow do string
        zestaw_motywow.append(motyw)             #dodawanie string do tabelki       
        motyw=''                                 #czyszczenie string
    return zestaw_motywow

assert motywo([[],[]])!=None, "petla w funkcji nie wykonuje sie"

if __name__ == "__main__":
    #Testy poprawnosci
    profil = [[0.2, 0.1],
              [0.4, 0.6],
              [0.3, 0.3],
              [0.1, 0.0]]
    tab = [0.3, 0.7, 0.0, 0.0]
    nukleo = motywo(profil)
    C = 0
    G = 0
    motyw = ''
    for i in range(0, len(nukleo)):
        if(nukleo[i][1]=='C'):
            C += 1
        if (nukleo[i][0] == 'G'):
            G += 1
    print("Dla czestosci 0.6|| Na 1000 nukleotydow, wystapienia C: ", C)
    print("Dla czestosci 0.3|| Na 1000 nukleotydow, wystapienia G: ", G)

    for x in range(0, 100):
        motyw += prawdo(tab)
    print("\n", motyw)
    C = motyw.count('C')
    A = motyw.count('A')
    print("Prawdopodobienstwo A: 0.3, procent wystapien A: ", A)
    print("Prawdopodobienstwo C: 0.7, procent wystapien C: ", C)
