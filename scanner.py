from network import scan_network
from portscan import scan_ports
from webcheck import detect_web_server, test_sqli, test_xss
from report import save_json, generate_html

def main():
    base = "192.168.0"
    results = {}

    hosts = scan_network(base)

    for h in hosts:
        ports = scan_ports(h)

        results[h] = {
            "ports": ports
        }

        if 80 in ports or 8080 in ports:
            url = f"http://{h}/"
            server = detect_web_server(url)
            results[h]["web"] = server

            results[h]["sqli"] = test_sqli(url + "?id=")
            results[h]["xss"] = test_xss(url + "?q=")

    save_json(results)
    generate_html(results)

if __name__ == "__main__":
    main()