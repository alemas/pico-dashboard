import socketpool
import adafruit_requests
import ssl

import wifi_manager

SOCKET_POOL = socketpool.SocketPool(wifi_manager.WIFI_RADIO)
REQUESTS = adafruit_requests.Session(SOCKET_POOL, ssl.create_default_context())

def __encode_space_characters(values):
    for value in values:
        if type(value) == str:
            value.replace(" ", "%20")

def __append_query_params_to_url(url: str, params: dict) -> str:
    url = f"{url}?"
    key_value = ["", ""]
    for param in params.items():
        if type(param[1]) == list:
            key_value[0] = param[0]
            for item in param[1]:
                key_value[1] = item
                __encode_space_characters(key_value)
                url = f"{url}&{key_value[0]}={key_value[1]}"
        else:
            __encode_space_characters(param)
            url = f"{url}&{param[0]}={param[1]}"
    return url
        

def get_quote() -> dict:
    url = "https://www.adafruit.com/api/quotes.php"
    response = REQUESTS.get(url)
    text = response.text
    response.close()
    del response
    return text

def get_forecast() -> dict:

    base_url = "https://api.open-meteo.com/v1/forecast"
    latitude = float(-29.17)
    longitude = float(-51.18)
    hourly = [
        "temperature_2m",
        "apparent_temperature", 
        "relativehumidity_2m",
        "precipitation_probability",
        "weathercode"
    ]

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": hourly
    }

    url = __append_query_params_to_url(base_url, params)
    print(url)
    response = REQUESTS.get(url=url)
    json = response.json()
    response.close()
    del response
    return json


