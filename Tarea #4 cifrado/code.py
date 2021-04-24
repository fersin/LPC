#!/usr/bin/env python3
import hashlib
import base64
from typing import Callable

def encode_decode_bytes(byte_message: bytes, encode_fn: Callable[[bytes], bytes]) -> bytes:
    return encode_fn(byte_message)


def encode_text(text: str, encoding_format: str = 'ascii') -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64encode).decode(encoding_format)


def decode_text(text: str, encoding_format: str = 'ascii') -> str:
    return encode_decode_bytes(text.encode(encoding_format), base64.b64decode).decode(encoding_format)


def encode_file(path:str) -> bytes:
    with open(path, 'rb') as file_to_encode:
        return encode_decode_bytes(file_to_encode.read(), base64.b64encode)


def decode_file(path:str) -> bytes:
    file_to_encode = open(path, 'rb')
    return encode_decode_bytes(file_to_encode.read(), base64.b64decode)


def save_file(path: str,content: bytes) -> None:
    with open(path, 'wb') as file_to_save:
        file_to_save.write(content)

def encode_plus_one(word:str) -> str:
    return "".join([chr(ord(character)+2) for character in word])

if __name__ == '__main__':
    import sys

    cmds = {'encode': base64.b64encode, 'decode': base64.b64decode}
    if len(sys.argv) > 1:
        main_cmd = sys.argv[1]
        encode_format = sys.argv[2] if len(sys.argv) > 2 else 'ascii'
        code_function = cmds.get(main_cmd, cmds.get('encode'))
        print(encode_decode_bytes(sys.stdin.read(), code_function))



    #msg encoded
    save_file('encoded_msg.txt', encode_file('msg.txt'))

    #fcfm image
    save_file('encoded_fcfm.txt', encode_file('fcfm.png'))

    #misterious images
    save_file('nonmystery1.png', decode_file('mystery_img.txt'))
    save_file('nonmystery2.png', decode_file('mystery_img2.txt'))
    
    #hash sha256sum
    fcfm='17b84bb63499d0a25cb2098da953ebbf2f7d597a5c03b69619d72de789e6844e' 

    mystery1='f80511dcd72cbfbf9e1a857f19e52b154124baa14a8d03fc10fa08be99406964'

    mystery2='b41664282332734436e93fe3c3e5261a0d1a2e93085d3e445168ab8abd94e5f4'

    msg='34dfde0dc0f3a2fab4c3ed0b19730547e7ab9c7a1272f28e4e8da3557b6c8f11'

    with open('fcfm.png',"rb") as f:
      bytes = f.read() # read entire file as bytes
      readable_hash = hashlib.sha256(bytes).hexdigest();
      print(readable_hash)
      if readable_hash==fcfm:
        print("todo bien carnal")
    with open('mystery_img.txt',"rb") as f:
      bytes = f.read() # read entire file as bytes
      readable_hash = hashlib.sha256(bytes).hexdigest();
      print(readable_hash)
      if readable_hash==mystery1:
        print("todo bien carnal")
    with open('mystery_img2.txt',"rb") as f:
      bytes = f.read() # read entire file as bytes
      readable_hash = hashlib.sha256(bytes).hexdigest();
      print(readable_hash)
      if readable_hash==mystery2:
        print("todo bien carnal")

    with open('msg.txt',"rb") as f:
      bytes = f.read() # read entire file as bytes
      readable_hash = hashlib.sha256(bytes).hexdigest();
      print(readable_hash)
      if readable_hash==msg:
        print("todo bien carnal :)")
        
