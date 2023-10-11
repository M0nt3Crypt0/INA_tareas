# Libraries 
import requests
import sys
import time

# Devices IP
SHELLY_PLUS_1_IP = "192.168.55.103"
SHELLY_PLUS_HT_IP = "192.168.55.102"

# Weather localization
LATITUD = 39.46975
LONGITUD = -0.37739

# GET to http://device/path
def get_api(device, path):
    url = f"http://{device}{path}"
    print(url)
    response = requests.get(url)
    return response

# Check connectivity to device
def check_device_connection(device):
    try:
        get_api(device, "/shelly")
    except:
        sys.exit(f"No connection to {device}")

# Turn on Shelly Plus 1 if off
def shelly_plus_on():
   status = get_api(SHELLY_PLUS_1_IP, "/relay/0").json()
   if status["ison"] == False:
       print("Enciende el relay")
       get_api(SHELLY_PLUS_1_IP, "/relay/0?turn=on")

# Turn off Shelly Plus 1 if on
def shelly_plus_off():
   status = get_api(SHELLY_PLUS_1_IP, "/relay/0").json()
   if status["ison"]:
       print("Enciende el relay")
       get_api(SHELLY_PLUS_1_IP, "/relay/0?turn=off")

def main():
    # Main loop
    while True:
        # Read internal temperature
        check_device_connection(SHELLY_PLUS_HT_IP)
        response_json = get_api(SHELLY_PLUS_HT_IP, "/rpc/Temperature.GetStatus?id=0").json()
        temp_in = response_json["tC"]
        print(temp_in)

        # Read external temperature 
        check_device_connection("api.open-meteo.com")
        response_json = get_api("api.open-meteo.com", f"/v1/forecast?latitude={LATITUD}&longitude={LONGITUD}&current=temperature_2m").json()
        temp_out = response_json["current"]["temperature_2m"]
        print(temp_out)

        # Turn on switch if temperature inside > outside
        if temp_in > temp_out:
            check_device_connection(SHELLY_PLUS_1_IP)
            shelly_plus_on()
        else:
            # Else turn off
            check_device_connection(SHELLY_PLUS_1_IP)
            shelly_plus_off()
        time.sleep(2)

if __name__ == '__main__':
    sys.exit(main())