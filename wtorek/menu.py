while True:
    print("MENU PROGRAMU")
    print("1. dodaj\n2. odejmij\nz - zakończ program")
    wybor = input('Wprowadź swój wybór: ')
    if wybor == "1":
        a = int(input("Podaj a:"))
        b = int(input("Podaj b:"))
        print(f"Suma dodawania={a + b}\n")
    elif wybor == "2":
        print("10-5=5\n")
    elif wybor == "z":
        break
    else:
        print("Nie ma takiej pozycji w menu!\n")

print("Dziękujemy za skorzystanie z naszego programu!")
