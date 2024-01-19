import math


def encode():
    keyname = input("Prefix of '-Public.key' file?\n")
    message = input(f"Enter message.\nMessages of a certain length will be impossible to decode. If you must send a large message, break it up.\n")
    encode_two = int.from_bytes(message.encode('utf-8'), byteorder='big', signed=False)
    with open(f'{keyname}-public.key', "r") as f:
        content = f.read()
        keymod, publick = content.split(",")
    encoded = pow(encode_two, int(publick), int(keymod), )
    with open('encode\encoded.txt', 'w') as file:
        file.write(str(encoded))
        file.close()
    print(encoded)
    input("Encoded message saved to /Encode/encoded.txt")


def decode():
    keyname = input("Prefix of '-Private.key' file?\n")
    encodedfile = input(f"Enter encoded file name as seen in /decoded/, including extension.\n")
    with open(f"decode\{encodedfile}", "r") as f:
        message = f.read()
    with open(f'{keyname}-private.key', "r") as f:
        content = f.read()
        keymod, privatek = content.split(",")
    decode_two = pow(int(message), int(privatek), int(keymod), )
    decoded = (int(decode_two)).to_bytes(math.ceil((int(decode_two)).bit_length() / 8), byteorder='big',
                                         signed=False).decode('utf-8')
    with open('decode\Output.txt', 'w') as file:
        file.write(str(decoded))
        file.close()
    input('Decoded message saved to /decode/output.txt')
