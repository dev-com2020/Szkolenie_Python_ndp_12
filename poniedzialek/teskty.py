a = 'Witaj "cyfrowy" Świecie'
#    0123456789101112131415...23

print(a)
b = '''Tutaj jest tekst         🧸🧸🧸
                    Tutaj też jest tekst        🧸🧸🧸
                   🧸🧸🧸             I tutaj również!'''
print(b)

print(len(a))
print(a[22])
print(a[0:5])  # slice
teskt1 = a[-7:]
teskt2 = a[:5]
print(teskt2 + " " + teskt1)

c = 'tomek!'

print(c.upper())
print(c.title())
print(c.endswith("!"))
print(c.startswith('t'))
print("indeks ! w napisie to:", c.index("!"))
print(f"indeks ! w napisie to: {c.index('!')}")
print("indeks ! w napisie to: %s " % c.index('!'))
print("indeks ! w napisie to: {} ".format(c.index('!')))
print("Łańcuchy są łączone \nza pomocą operatora plus \n\t\b(+):")

liczba1 = "5"
liczba2 = 5
liczba3 = "a"  # tak sie nie da zrzutować
suma = int(liczba1) + liczba2
print(suma)
print(liczba3 * 10)

python = 3.1000001

print("Moja wersja Pythona to:", python)
print(f"Moja wersja Pythona to: {python:0.2f}")
# print("Moja wersja Pythona to: {}".format(python, '0.2f'))

