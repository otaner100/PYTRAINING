## Nome da classe: CiscoDevice
## Atributos: ip, username, password
## Metodos: executar comandos, parse (analisar) outputs

class CiscoDevice:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

r1 = CiscoDevice('192.168.56.121', 'admin', 'admin')

print(dir(r1))