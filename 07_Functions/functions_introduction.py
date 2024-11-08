import random
import string

def cred(user, priv):
    senha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return f"usuario: {user}, privilegio {priv} e senha {senha}"

# with open ("credenciais.txt", "w") as file: # arwuivo credencias e escreve
#     file.write(cred('renato', 15))
#     file.write(cred('bia', 7))
ulist = ['renato', 15]
udict = {'user':'renato', 'priv': 15}

print(cred('renato', 15), ('  padrao'))
print(cred(user='renato', priv=14), ('  especificando o user e priv'))
print(cred(*ulist), ('  *lista'))
print(cred(*['admin', 16]), ('  lista modificada'))
print(cred(**udict), ('  **dict'))
print(cred(**{'user':'admin', 'priv': 18}), ('  dict modificado'))


ulist2 = ['show ip bri', 'show ver', 'conf t']

def credargs(user, priv, *args):
    senha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    print(f"usuario: {user}, privilegio {priv} e senha {senha}")
    print('os comandos são...')
    for cmd in ulist2:
        print(cmd)

credargs('renato',15, *ulist2)


dictusers = [{'user':'renato', 'priv': 15},
             {'user':'andre', 'priv':16},
             {'user':'vitoria', 'priv':7}]
def userscred(*args):
    list_users = []

    senha = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))

    for user in args:
        usuarios = f"usuario: {user['user']}, privilegio {user['priv']} e senha {senha}"
        list_users.append(usuarios)
    return list_users
print(userscred(*dictusers))
