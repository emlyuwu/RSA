from Crypto.Util import number


def generate_keys():

    global publick
    global privatek
    global keymod
    blength = 2048
    p = number.getPrime(blength)
    q = number.getPrime(blength)
    keymod = p * q
    phi_n = (p - 1) * (q - 1)
    publick = 65537
    privatek = pow(publick, -1, phi_n)


def print_keys():
    print(publick)
    print(privatek)
    print(keymod)


def write_keys():
    with open('public.key', 'w') as file:
        file.write(f"{keymod},{publick}")
        file.close()
    with open('private.key', 'w') as file:
        file.write(f"{keymod},{privatek}")
        file.close()


def ext_run():
    generate_keys()
    write_keys()
    input("Complete. Written to .key files.")
