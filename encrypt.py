import secrets

def generate_keys():
    key_list = []
    for i in range(20):
        key = str(secrets.token_bytes(64))
        key_list.append(key)
    return key_list


def encryption(key, message):
    secret = ''
    for a, b in zip(key, message):
        e = chr(ord(a) ^ ord(b))
        secret += e
    return secret


def decryption(key, secret):    
    message = ''
    for a, b in zip(key, secret):
        d = chr(ord(a) ^ ord(b))
        message += d
    return message


def Main():
    key_list = generate_keys()
    our_message = 'Hello!'
    
    while len(key_list) > 0:
        enc_msg = encryption(key_list[0], our_message)
        print(enc_msg.encode())
        dec_msg = decryption(key_list[0], enc_msg).encode()
        print(dec_msg)
        key_list.pop(0)
    print(len(key_list))


if __name__ == '__main__':
    Main()
