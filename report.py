import json

def save_json(data, path="results.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def generate_html(data, path="report.html"):
    html = "<html><body><h1>Relatório do Scanner</h1>"
    for host, info in data.items():
        html += f"<h2>{host}</h2>"
        html += f"<p>OS: {info.get('os','?')}</p>"
        html += "<ul>"
        for p in info.get("ports", []):
            html += f"<li>Porta {p}</li>"
        html += "</ul>"
        if info.get("web"):
            html += f"<p>Servidor Web: {info['web']}</p>"
        if info.get("sqli"):
            html += "<p style='color:red'>Possível SQL Injection</p>"
        if info.get("xss"):
            html += "<p style='color:red'>Possível XSS</p>"
    html += "</body></html>"
    with open(path, "w") as f:
        f.write(html)