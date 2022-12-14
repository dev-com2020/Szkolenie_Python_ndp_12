import json

lista = []

with open('bohaterowie.json', 'r') as f:
    data = json.load(f)

# print(data)
# print(data['members'])
# print(data['members'][2])
# print(data['members'][2]['powers'])
# lista.append(data['members'][2]['powers'][3])

for i in data['members']:
    lista.append(i)

with open('bohaterowie2.json', 'w') as f:
    data = json.dump(lista, f, indent=4)

# print(lista)
for i in lista:
    print(i)
