import tkinter as tk
import subprocess

def run_scan():
    subprocess.run(["python", "scanner.py"])

root = tk.Tk()
root.title("Python Vulnerability Scanner")

btn = tk.Button(root, text="Iniciar Scan", command=run_scan)
btn.pack(padx=20, pady=20)

root.mainloop()