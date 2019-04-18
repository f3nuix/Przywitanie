imie = input("Jak masz na imie:")

print("Witaj "+imie+" w moim programie!

print("Sprawdz ile dwojek miesci sie w podanej przez ciebie liczbie!")


liczba = int(input("Podaj liczbe: "))

ilosc_dwojek = 0


while liczba >= 2:
    liczba = liczba - 2
    ilosc_dwojek +=1

print(ilosc_dwojek)