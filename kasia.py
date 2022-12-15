from numpy.core.defchararray import islower


def sprawdz_haslo(haslo):
        if len(haslo) < 6:
            if islower(haslo) == True:
                return "Twoje hasło jest zbyt krótkie i nie zawiera wilkich liter.\nJeśli chcesz możesz spróbuj ponownie."
            elif islower(haslo) == False:
                return "Twoje hasło jest zbyt krótkie.\nJeśli chcesz możesz spróbuj ponownie."
        elif len(haslo) > 7:
            if islower(haslo) == True:
                return "Twoje hasło nie zawiera wilkich liter.\nJeśli chcesz możesz spróbuj ponownie."
            elif islower(haslo) == False:
                return "Twoje hasło jest OK 👍"



print("Witaj !!!")
print("Program sprawdzi moc twojego hasła.")
print("Jeśli chcesz zweryfikowac swoje haslo wpisz 1:\nJeśli chcesz zakończyć wpisz 2:")
while True:
    wybor = input('Wprowadź swój wybór: ')
    if wybor == "1":
        while True:
            wynik = sprawdz_haslo(input("Podaj swoje hasło: "))
            print(wynik)
            if wynik == "Twoje hasło jest OK 👍":
                break
    elif wybor == "2":
        break
    else:
        print("Nie ma takiej pozycji w menu!")
