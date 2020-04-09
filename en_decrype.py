from Crypto.Cipher import AES
import os
import hashlib
import base64
'''
reference:
https://stackoverflow.com/questions/53320143/pycryptodome-aes-cbc-encryption-does-not-give-desired-output
https://blog.csdn.net/sinat_37967865/article/details/100125445
https://samkuo.me/post/2015/09/python-aes-256-and-sha-256-examples/?fbclid=IwAR3Mr9WPKMpPjLr-3P6DVr7suG6GMIXCC3oTbTTRR0pQ4b5-mEg4wwiKvns
'''


DEFAULT_ENTROPY = 32

def add_to_32(value):
    while len(value) % 32 != 0:
            value += b'\x00'
    return value     

#將使用者輸入的帳號轉換為32bytes
def cut_value(org_str):
    org_bytes = str.encode(org_str)
    n = int(len(org_bytes) / 32)
    i = 0
    new_bytes = b''
    while n >= 1:
        i = i + 1
        new_byte = org_bytes[(i-1)*32:32*i-1]
        new_bytes += new_byte
        n = n - 1
    if len(org_bytes) % 32 == 0:                   
        all_bytes = org_bytes
    elif len(org_bytes) % 32 != 0 and n>1:         
        all_bytes = new_bytes + add_to_32 (org_bytes[i*32:])
    else:
        all_bytes = add_to_32 (org_bytes)          
    return all_bytes

#隨機值iv寫死，無不斷變更加密後的結果之需求
def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CBC, iv=b'0123456789abcdef')
    encrypt_aes = cryptor.encrypt(cut_value(data))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  
    return encrypted_text

def aes_decrypt(secret_str, key):
    cryptor = AES.new(key, AES.MODE_CBC, iv=b'0123456789abcdef')
    base64_decrypted = base64.decodebytes(secret_str.encode(encoding='utf-8'))
    # 解密轉回str
    decrypted_text = str(cryptor.decrypt(base64_decrypted), encoding='utf-8')
    return decrypted_text

#隨機產生key，for test.
def token_bytes():
    nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)

#隨機產生key，加上存檔，並且刪除原先的加密檔案(須重產)
def generate_key():
    nbytes = DEFAULT_ENTROPY
    key  = token_bytes()
    with open('key.key','wb+') as f:
        f.write(key)
    os.remove('encrype.config')
    return None

def get_key():
    with open('key.key', 'rb+') as outfile:
        return outfile.read()

