import argparse
import sys


def liczby(number, other_number, output):
    wynik = number + other_number
    print(f"Wynik dodawania wynosi: {wynik}", file=output)


parser = argparse.ArgumentParser()
parser.add_argument('-n1', type=int, help='Liczba 1', default=1)
parser.add_argument('-n2', type=int, help='Liczba 2', default=1)
parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Plik na dane wyjściowe', default=sys.stdout)
args = parser.parse_args()

liczby(args.n1, args.n2, args.output)
