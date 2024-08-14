import requests


class MapaUtils():

    @staticmethod
    def obtener_ruta(lat_origen, lon_origen, lat_destino, lon_destino):
        url = f"https://router.project-osrm.org/route/v1/driving/{lon_origen},{lat_origen};{lon_destino},{lat_destino}?steps=true"
        response = requests.get(url)
        if response.status_code == 200:
            ruta = response.json()
        lista_coordenadas = []
        if ruta:
            for step in ruta["routes"][0]["legs"][0]["steps"]:
                lista_coordenadas.append((step["maneuver"]["location"][1], step["maneuver"]["location"][0]))
        else:
            print("Error al obtener la ruta")
        return lista_coordenadas
