import requests

odp = requests.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Kielce&aqi=no')
print(odp.status_code)
plik = odp.json()['location']['name']
plik2 = odp.json()['current']['temp_c']
print(plik)
print(plik2)