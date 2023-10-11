# Bibliotecas 
import requests
import json
import sys

# Config
SHELLY_PLUS_1_IP = "192.168.55.103"

SHELLY_PLUS_HT_IP = "192.168.55.102"
SHELLY_DW_IP = "z"

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
    try:
        response = get_api(device, "/shelly")
    except:
        sys.exit("No connection")
    if not response.ok:
        sys.exit("Error no response")

def shelly_plus_on():
   status = get_api(SHELLY_PLUS_1_IP, "/relay/0").json()
   if status["ison"] == False:
       print("Enciende el relay")
       get_api(SHELLY_PLUS_1_IP, "/relay/0?turn=on")


def shelly_plus_off():
   status = get_api(SHELLY_PLUS_1_IP, "/relay/0").json()
   if status["ison"]:
       print("Enciende el relay")
       get_api(SHELLY_PLUS_1_IP, "/relay/0?turn=off")

# Main
def main():
    error = False
    error_msg = ""


    while not error:
        
        # Lee temperatura interna
        check_device_connection(SHELLY_PLUS_HT_IP)
        response_json = get_api(SHELLY_PLUS_HT_IP, "/rpc/Temperature.GetStatus?id=0").json()
        temp = response_json["tC"]
        print(temp)

        # Lee si la 'ventana' está abierta
        #check_device_connection(SHELLY_DW_IP)
        #response = get_api(SHELLY_DW_IP, "/status")
        #print(response.json())
        #response_json = json.load(response)
        #open = response_json[]

        # Lee temperatura externa 
        # TODO

        # Si temp > 30 o puerta abierta enciende
        if temp > 20:
            check_device_connection(SHELLY_PLUS_1_IP)
            shelly_plus_on()
        # else apaga
        else:
            shelly_plus_off()
    
    sys.exit(error_msg)

if __name__ == '__main__':
    sys.exit(main())