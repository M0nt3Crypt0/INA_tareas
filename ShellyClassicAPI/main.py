# Bibliotecas 
import requests
import json
import sys


# Config
SHELLY_PLUS_1_IP = "192.168.55.103"

SHELLY_PLUS_HT_IP = "192.168.55.102"
SHELLY_DW_IP = "192.168.55.105"

LATITUD = 39.46975
LONGITUD = -0.37739

# Funciones
def get_api(device, path):
    url = f"http://{device}{path}"
    response = requests.get(url)
    return response

def post_api(device, path, payload):
    url = f"http://{device}{path}"
    response = requests.post(url, json=payload)
    return response.status_code == 200

def check_device_connection(device):
    response = get_api(device, "/shelly")
    return response.ok()

# Main
def main():
    error = False

    check_device_connection(SHELLY_PLUS_1_IP)
    if error:
        error_msg = "No se puede conectar a Shelly Plus 1"
    check_device_connection(SHELLY_PLUS_HT_IP)
    if error:
        error_msg = "No se puede conectar a Shelly Plus HT"
    check_device_connection(SHELLY_DW_IP)
    if error:
        error_msg = "No se puede conectar a Shelly DW"

    while not error:
        # Lee temperatura interna
        

        # Lee temperatura externa 

        # Lee si la 'ventana' está abierta
        

        # Si temp > 30 o puerta abierta enciende
        if temp > 30 or open:
            set_value(SHELLY_PLUS_1_IP, "relay/0", {"turn": "on"})
        # else apaga
        else:
            set_value(SHELLY_PLUS_1_IP, "relay/0", {"turn": "off"})
    
    sys.exit(error_msg)