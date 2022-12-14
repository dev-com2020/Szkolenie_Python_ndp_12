import json
import keyword

print(keyword.kwlist)

person = {"name": "Bob",
          "languages": ["English", "French"],
          "age": 32,
          "programs_lang": {1: "Python", 2: ['Java', 'JS']},
          "smoke": False,
          "children": None
          }

with open('dane.json', 'w') as plik:
    json.dump(person, plik, indent=4)


