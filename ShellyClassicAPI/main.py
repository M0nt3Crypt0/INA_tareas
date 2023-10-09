# Bibliotecas 
import requests
import json


# Config
SHELLY_PLUS_1_IP = "192.168.55.103"

SHELLY_PLUS_HT_IP = "192.168.55.102"
SHELLY_PLUS_DW_IP = "192.168.55.105"

# Funciones
def check_connection_to(ip):
    url = f"http://{ip}/shelly"
    response = requests.get(url)
    return response.ok

def get_value(ip, key):
    url = f"http://{ip}/{key}"
    response = requests.get(url)
    return response.json

def set_value(ip, key, payload):
    url = f"http://{ip}/{key}" 
    response = requests.post(url, json=payload)
    return response.status_code == 200

# Main
def main():
    # Si temp > 30 o puerta abierta enciende
    if temp > 30 or open:
        set_value(SHELLY_PLUS_1_IP, "relay/0", {"turn": "on"})
    # else apaga
    else:
        set_value(SHELLY_PLUS_1_IP, "relay/0", {"turn": "off"})