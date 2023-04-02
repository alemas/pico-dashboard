import socketpool
import adafruit_requests
import ssl

import wifi_manager

SOCKET_POOL = socketpool.SocketPool(wifi_manager.WIFI_RADIO)
REQUESTS = adafruit_requests.Session(SOCKET_POOL, ssl.create_default_context())

def get_quotes() -> str:
    url = "https://www.adafruit.com/api/quotes.php"
    response = REQUESTS.get(url)
    text = response.text
    response.close()
    del response
    return text



