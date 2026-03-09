# 🛰️ Advanced Python Network Scanner

Um **scanner de rede avançado em Python** com interface estilo terminal hacker, suporte a **multithreading**, detecção de portas abertas e testes básicos de conectividade.

Este projeto foi desenvolvido para fins **educacionais**, ajudando a entender conceitos de:

* redes de computadores
* segurança da informação
* sockets em Python
* programação concorrente (threads)

---

# 📌 Funcionalidades

O scanner possui diversas funcionalidades úteis para estudo de redes e segurança.

### ⚡ Scanner de Portas Multithread

Escaneia **até 1024 portas simultaneamente** usando múltiplas threads, tornando o processo muito mais rápido.

Exemplo de saída:

```
[ABERTA] Porta 22
[ABERTA] Porta 80
[ABERTA] Porta 443
```

---

### 🌐 Teste de Conectividade (Ping)

Permite verificar rapidamente se um host está ativo na rede.

```
[+] Verificando host...
[HOST ATIVO]
```

---

### 🎨 Interface Estilo Terminal Hacker

O scanner possui:

* cores no terminal
* banner ASCII
* menu interativo

Exemplo do banner exibido:

```
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝
```

---

# 🧠 Portas Monitoradas

O scanner verifica as **1024 primeiras portas TCP**.

Algumas portas comuns:

| Porta | Serviço |
| ----- | ------- |
| 21    | FTP     |
| 22    | SSH     |
| 23    | Telnet  |
| 25    | SMTP    |
| 53    | DNS     |
| 80    | HTTP    |
| 110   | POP3    |
| 139   | NetBIOS |
| 143   | IMAP    |
| 443   | HTTPS   |

---

# 📂 Estrutura do Projeto

```
advanced-network-scanner
│
├── scanner.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Tecnologias Utilizadas

* Python 3
* sockets
* multithreading
* queue
* colorama

Biblioteca adicional:

```
colorama
```

---

# 📦 Instalação

Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/advanced-network-scanner.git
```

Entre na pasta do projeto:

```
cd advanced-network-scanner
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o scanner com:

```
python scanner.py
```

Menu exibido:

```
==============================
      HACKER NETWORK PANEL
==============================

1 - Scan de portas
2 - Testar host (Ping)
3 - Limpar tela
0 - Sair
```

---

# 🎯 Objetivo Educacional

Este projeto ajuda a praticar:

* programação em Python
* conceitos de redes
* comunicação TCP
* segurança ofensiva e defensiva
* programação concorrente

---

# ⚠️ Aviso

Este projeto é **exclusivamente para fins educacionais**.

Não utilize scanners de rede em sistemas sem autorização.

O uso indevido pode violar leis de segurança digital.

---

# 🚀 Possíveis Melhorias Futuras

Algumas evoluções possíveis para o projeto:

* scan automático de rede (192.168.0.0/24)
* detecção de sistema operacional
* identificação de versões de serviços
* exportar resultados para JSON
* gerar relatórios HTML
* interface gráfica

---

# 👨‍💻 Autor

*** Julio Cesar Alves de Oliveira ***

Estudante de redes de computadores, programação e segurança da informação.

---
