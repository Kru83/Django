import  requests

def ipAddress():
    ipAddressData = None
    ipAddressRequest = "http://www.geoplugin.net/json.gp"
    ipAddressResponse = requests.get(ipAddressRequest)
    ipAddressStatus = ipAddressResponse.status_code

    if ipAddressStatus == 200:
        ipAddressData = ipAddressResponse.json()
    else:
        print(F"Error {ipAddressStatus}")
    return ipAddressData