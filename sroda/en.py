import json

with open('../dane/bohaterowie.json', 'r') as f:
    data = json.load(f)

lista = []
for index, wartosc in enumerate(data['members']):
    print(index, wartosc)
