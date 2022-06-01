import hashlib
import secrets


def register(password) -> (str, str):
    salt = secrets.token_hex(16)
    salted_password = password + salt

    h = hashlib.new('sha256')
    h.update(salted_password.encode())
    passwoord_hash = h.hexdigest()
    return passwoord_hash, salt


def check(password, hash, salt) -> bool:
    checking = password + salt

    h = hashlib.new('sha256')
    h.update(checking.encode())
    pass_hash = h.hexdigest()

    return hash == pass_hash



password = input('Enter your password: ')

p_hash, salt = register(password)

print('Registered successfully')

password = input('Login, enter password: ')

res = check(password, p_hash, salt)

if res:
    print('Logged in successfully')
else:
    print('Try again')