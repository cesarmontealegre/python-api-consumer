import requests

url = 'https://api.github.com/users/cesarmontealegre'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    name = data['name']
    location = data['location']
    bio = data['bio']
    print(f"Nombre: {name}")
    print(f"Ubicación: {location}")
    print(f"Bio: {bio}")
else:
    print("No se pudo obtener la información del usuario.")