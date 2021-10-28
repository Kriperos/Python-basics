

class Pizza:
    def __init__(self, nazwa, ciasto, skladniki, sosy, pokrojona):
        self.ciasto = ciasto
        self.skladniki = skladniki
        self.sosy = sosy
        self.nazwa = nazwa
        self.pokrojona = pokrojona        

    def pokaz_recepte(self):
        print(f"Pizza {self.nazwa}")
        print(f"Ciasto: {self.ciasto}")
        print(f"Skladniki: {self.skladniki}")
        print(f"Sosy: {self.sosy}")
        print(f"Pokrojona: {self.pokrojona}")

pizza_hawajska = Pizza("Hawajska", "grube", ["ananas", "szynka"], ["pomidorowy",], False)

#pizza_hawajska.pokaz_recepte()

pizza_wege = Pizza("Wegetarianska", "cienkie", ["kukurydza", "pieczarki", "pomidor"], ["czosnkowy"], True)

#pizza_wege.pokaz_recepte()

class PozycjaZamowienia:
    def __init__(self, pizza, ilosc):
        self.pizza = pizza
        self.ilosc = ilosc

OCZEKIWANIE = 0
W_TRAKCIE_REALIZACJI = 1
GOTOWE = 2
W_TRAKCIE_DOSTAWY = 3
DOSTARCZONE = 4

class Zamowienie:

    status_zamowienia = OCZEKIWANIE
    numer = 11

    def __init__(self, pozycje_zamowienia, adres, imie, nazwisko, telefon):
        self.pozycje_zamowienia = pozycje_zamowienia
        self.adres = adres
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def wyslij_do_kuchni(self):
        self.status_zamowienia = W_TRAKCIE_REALIZACJI

    def wyslij_zamowienie(self):
        self.status_zamowienia = W_TRAKCIE_DOSTAWY

pozycje_zamowienia = [PozycjaZamowienia(pizza_hawajska, 2), 
                      PozycjaZamowienia(pizza_wege, 1)]


#for pozycja in pozycje_zamowienia:    
#    print(f"Pizza: {pozycja.pizza.nazwa}")
#    print(f"Ilosc: {pozycja.ilosc}")

zamowienie = Zamowienie(pozycje_zamowienia, "os. Stare Sady 31/8 Piotrkow Tryb.", "Tomasz", "Szkudlarek", "+48 600 407 664")
zamowienie.wyslij_do_kuchni()
pass