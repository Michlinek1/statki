import time
import webbrowser
from termcolor import colored
Plansza = (  
 "A1 " "a2 " "a3 " "a4 " "a5 " "a6 " "a7 " "a8 " "a9 " "a10 ""\n"
 "B1 " "b2 " "b3 " "b4 " "b5 " "b6 " "b7 " "b8 " "b9 " "b10""\n"
 "C1 " "c2 " "c3 " "c4 " "c5 " "c6 " "c7 " "c8 " "c9 " "c10""\n"
 "D1 " "d2 " "d3 " "d4 " "d5 " "d6 " "d7 " "d8 " "d9 " "d10 ""\n" 
 "E1 " "e2 " "e3 " "e4 " "e5 " "e6 " "e7 " "e8 " "e9 " "e10 ""\n" 
 "F1 " "f2 " "f3 " "f4 " "f5 " "f6 " "f7 " "f8 " "f9 " "f10 ""\n"
 "G1 " "g2 " "g3 " "g4 " "g5 " "g6 " "g7 " "g8 " "g9 " "g10 ""\n"
 "H1 " "h2 " "h3 " "h4 " "h5 " "h6 " "h7 " "h8 " "h9 " "h10 ""\n" 
 "I1 " "i2 " "i3 " "i4 " "i5 " "i6 " "i7 " "i8 " "i9 " "i10 ""\n" 
 "J1 " "j2 " "j3 " "j4 " "j5 " "j6 " "j7 " "j8 " "j9 " "j10 "
)
print(Plansza)
Pozycje = []
Gracz1Poz = []
BotRundy = 8 

def Main():
    print("Witaj w Grze: Statki:")
    PytNazwa = input("Jak chcesz się nazywać?" + "\n")
    print(f"Witaj {PytNazwa}")
    print("Zasady:")
    time.sleep(0.5)
    #webbrowser.open("https://pppp.walbrzych.pl/gra-w-statki,185,pl#:~:text=Na%20jednej%20planszy%20gracz%20rysuje,zakr%C4%99cone%E2%80%9D%20czyli%20przypomina%C4%87%20litery%20L.")
    print("Zaczynamy!")
    for x in range(2):
        PytPozycje = input("Wybierz miejsce, w którym chcesz postawić swój dwumiejscowy statek" + "\n" )
        Pozycje.append(PytPozycje)
        Gracz1Poz.append(Gracz1Poz)
        
        
    ZmianaListDoString = ' '.join(Pozycje) #Zamienia liste na string
    cos = Plansza.replace(ZmianaListDoString, colored("=", 'red'))    
    print(cos)

           
            
Main()
