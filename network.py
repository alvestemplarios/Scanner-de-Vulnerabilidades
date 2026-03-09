import socket
import threading
from queue import Queue

COMMON_PORTS = [21,22,23,25,53,80,110,139,143,443,3306,8080]

def scan_ports(host):
    open_ports = []
    q = Queue()

    for p in COMMON_PORTS:
        q.put(p)

    def worker():
        while not q.empty():
            port = q.get()
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((host, port)) == 0:
                    open_ports.append(port)
                s.close()
            except:
                pass
            q.task_done()

    threads = []
    for _ in range(30):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    q.join()
    return open_ports