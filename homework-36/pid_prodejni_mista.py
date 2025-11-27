import json
from urllib import request

url_address_prodejni_mista = 'https://data.pid.cz/pointsOfSale/json/pointsOfSale.json'
url_address_ciselnik = 'https://data.pid.cz/pointsOfSale/json/consts-cs.json'
json_data = 'pid_prodejni_mista.json'
json_cislenik = 'pid_cislenik.json'


def get_pid_data(url, json_file_path):

    with request.urlopen(url) as response:
        data = json.load(response)
    
    with open(json_file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file)


def read_pid_data(json_file_path):
    with open(json_file_path, mode='r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    
    return loaded_data


def convert_int_to_days(number):
    days = {
        0: 'pondělí',
        1: 'úterý',
        2: 'středa',
        3: 'čtvrtek',
        4: 'pátek',
        5: 'sobota',
        6: 'neděle'
    }

    return days[number]


def generate_page(item):
    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
    <title>Document</title>
</head>
<body>
    <h1>Nazev: {item['name']}</h1>
    <p>Adresa: {item['address']}</p>
    <p>Oteviraci doba: {convert_int_to_days(item['openingHours'][0]['from'])} - {convert_int_to_days(item['openingHours'][0]['to'])}, <b>{item['openingHours'][0]['hours']}</b></p>

    <div id="map" style="height: 200px; border-radius: 6px;"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
    <script>
        const map = L.map('map').setView([{item['lat']}, {item['lon']}], 13);

        L.tileLayer('https://tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
                attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            }}).addTo(map);
        
        const marker = L.marker([{item['lat']}, {item['lon']}]).addTo(map);
    </script>
</body>
</html>
    '''

    with open(f'html-pages/{item["name"]}.html', mode='w', encoding='utf-8') as file:
        file.write(html)


def generate(num_of_places):
    data = read_pid_data(json_data)
    count = 0

    for item in data:
        if count >= num_of_places:
            break
        generate_page(item)
        count += 1

if __name__ == '__main__':
    get_pid_data(url_address_ciselnik, json_cislenik)
    get_pid_data(url_address_prodejni_mista, json_data)
    generate(5)