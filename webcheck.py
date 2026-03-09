import requests

def detect_web_server(url):
    try:
        r = requests.get(url, timeout=3)
        server = r.headers.get("Server", "Desconhecido")
        return server
    except:
        return None