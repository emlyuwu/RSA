from consolemenu import *
from consolemenu.items import *
from Crypto.Util import number
import math
import os

if not os.path.exists("keys"):
    os.makedirs("keys")


def generate_keys():
    global wkeyname
    wkeyname = input("What should the keys be named?\n")
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
    with open(f'keys/{wkeyname}-public.key', 'w') as file:
        file.write(f"{keymod},{publick}")
        file.close()
    with open(f'keys/{wkeyname}-private.key', 'w') as file:
        file.write(f"{keymod},{privatek}")
        file.close()


def ext_run():
    generate_keys()
    write_keys()
    input("Complete. Written to .key files.")


def encode():
    ckeyname = input("Key name? (prefix of '-public.key')\n")
    message = input(f"Enter message.\nMessages of a certain length will be impossible to decode. If you must send a "
                    f"large message, break it up.\n")
    encode_two = int.from_bytes(message.encode('utf-8'), byteorder='big', signed=False)
    with open(f'keys/{ckeyname}-public.key', "r") as f:
        content = f.read()
        keymod, publick = content.split(",")
    encoded = pow(encode_two, int(publick), int(keymod), )
    if not os.path.exists("encode"):
        os.makedirs("encode")
    with open('encode\encoded.txt', 'w') as file:
        file.write(str(encoded))
        file.close()
    print(encoded)
    input("Encoded message saved to /encode/encoded.txt")


def decode():
    ckeyname = input("Key name? (prefix of '-private.key')\n")
    encodedfile = input(f"Enter message, or the location of the message with the prefix /.\n")
    if encodedfile.startswith("/"):
        encodedfile = encodedfile.split("/", 1)[1]
        with open(f"{encodedfile}", "r") as f:
            message = f.read()
    else:
        message = encodedfile
    with open(f'keys/{ckeyname}-private.key', "r") as f:
        content = f.read()
        keymod, privatek = content.split(",")
    decode_two = pow(int(message), int(privatek), int(keymod), )
    decoded = (int(decode_two)).to_bytes(math.ceil((int(decode_two)).bit_length() / 8), byteorder='big',
                                         signed=False).decode('utf-8')
    print(decoded)
    willwrite = input(
        "If you would like to write the decoded message to a file, enter a file name with the prefix #.\n")
    if willwrite.startswith('#'):
        willwrite = willwrite.split("#", 1)[1]
        if not os.path.exists("decode"):
            os.makedirs("decode")
        with open(f'decode/{willwrite}.txt', 'w') as file:
            file.write(str(decoded))
            file.close()
        input(f'Decoded message saved to /decode/{willwrite}.txt')
    else:
        input("Decoded message not saved.")


menu = ConsoleMenu("Cryptography tools by an idiot", "Ensure that keys are stored in subfolder /keys/.",
                   exit_menu_char="0")

RSAGEN = FunctionItem("Generate RSA Keys", ext_run, menu=menu, should_exit=False, menu_char="5")
encode = FunctionItem("Encode messages with RSA keys.", encode, menu=menu, should_exit=False,
                      menu_char="6")
decode = FunctionItem("Decode messages with RSA keys.", decode, menu=menu, should_exit=False,
                      menu_char="7")

menu.append_item(RSAGEN)
menu.append_item(encode)
menu.append_item(decode)

menu.show()
