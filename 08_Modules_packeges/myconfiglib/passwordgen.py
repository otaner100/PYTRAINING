import random
import string

def userGen (user, priv):
    secret = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return f'username {user} privi {priv} secret {secret}'

def userArgsGen (*args):
    list_user = []
    secret = random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)

    for user in args:
        usuario = f'username {user['user']} priv {user['priv']} secret {secret}'
        list_user.append(usuario)
    return list_user