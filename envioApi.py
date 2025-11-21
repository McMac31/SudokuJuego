import requests

def enviarPartida(datos):
    url_profesor = "http://192.168.25.133:8000/registrar_partida"
    try:
        respuesta=requests.post(url_profesor,json=datos)
        if respuesta==200:
            print("Datos enviados correctamente")
        else:
            print(f"{respuesta.status_code}:{respuesta.text}")
    except Exception as e:
        print(f"Error conectando {e}")