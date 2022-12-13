import argparse
import sys
import time


def liczby(number, other_number, output):
    wynik = number + other_number
    local_time = time.ctime()
    print(f"Wynik dodawania wynosi: {wynik}", file=output)
    print(f'Stempel czasowy={local_time}', file=output)


parser = argparse.ArgumentParser()
parser.add_argument('-n1', type=int, help='Liczba 1', default=1)
parser.add_argument('-n2', type=int, help='Liczba 2', default=1)
parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Plik na dane wyjściowe', default=sys.stdout)
args = parser.parse_args()

liczby(args.n1, args.n2, args.output)
