import requests

SQL_PAYLOAD = "' OR '1'='1"
XSS_PAYLOAD = "<script>alert(1)</script>"

def test_sqli(url):
    try:
        r = requests.get(url + SQL_PAYLOAD, timeout=3)
        if "sql" in r.text.lower() or "syntax" in r.text.lower():
            return True
    except:
        pass
    return False

def test_xss(url):
    try:
        r = requests.get(url + XSS_PAYLOAD, timeout=3)
        if XSS_PAYLOAD in r.text:
            return True
    except:
        pass
    return False