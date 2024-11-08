from paramiko import client
import time
from passwordgen import userGen, userArgsGen

comando_user = [userGen('lucas', 15), 'do show run | i usern']
'''comando_users = userArgsGen([{'user':'amanda','priv':7},
                 {'user':'joao','priv':8},
                 'do show run | i user'])'''

comandos_base = ['conf t']
def ciscoAcess(roteador, commands, user, secret):
    sshclient = client.SSHClient()
    sshclient.set_missing_host_key_policy(client.AutoAddPolicy())
    sshclient.connect(hostname=roteador, port=22, username=user, password=secret, look_for_keys=False, allow_agent=False)
    print("conectado com sucesso")
    device_invokeSSH = sshclient.invoke_shell()
    device_invokeSSH.send("terminal len 0\n")
    for i in comandos_base:
        device_invokeSSH.send(f"{i}\n")
        time.sleep(2)
    for cmd in commands:
        device_invokeSSH.send(f"{cmd}\n")
        time.sleep(3)
        output = device_invokeSSH.recv(65535)
        print(output.decode(), end="")

#ciscoAcess('192.168.56.120',comando_user , 'admin', 'admin')

# if __name__ == '__main__':
teste_main = userGen('carlos', 15)
print(__name__)
print(teste_main)