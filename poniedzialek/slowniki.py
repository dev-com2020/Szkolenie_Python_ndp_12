location = {"name": "Kielce",
            "region": ["SW", "MZ", "ZP"],
            "country": "Poland",
            "lat": 50.83,
            "lon": 20.67,
            "tz_id": "Europe/Warsaw",
            "localtime_epoch": 1670852840,
            "zbior": {'jeden': 2022, 'dwa': 2023},
            "localtime": "2022-12-12 14:47"}

print(location['tz_id'])
location['name'] = 'Gdynia'
location['opady'] = 100
location[1] = 1000
# print(location['name'])
print(location)
print(location.keys())
print(location.values())
print(location.items())
print(location['region'][0])
print(location["zbior"]['dwa'])
