from Crypto.Cipher import AES
import os
import hashlib
import base64
import json
'''
reference:
https://stackoverflow.com/questions/53320143/pycryptodome-aes-cbc-encryption-does-not-give-desired-output
https://blog.csdn.net/sinat_37967865/article/details/100125445
https://samkuo.me/post/2015/09/python-aes-256-and-sha-256-examples/?fbclid=IwAR3Mr9WPKMpPjLr-3P6DVr7suG6GMIXCC3oTbTTRR0pQ4b5-mEg4wwiKvns
'''

DEFAULT_ENTROPY = 32


def read_control():
    with open(r'AES256\Control.txt',encoding='UTF-8-sig',mode='r') as config:
        config_detail = config.readlines()
        status = 0
        for config in config_detail:
            if status ==0:
                key_path = config.split('->')[1]
                key_path = key_path.replace(r'\n','')
                status+=1
            else:
                result_path = config.split('->')[1]
                result_path = result_path.replace(r'\n','')
    return key_path,result_path



def add_to_32(value):
    while len(value) % 32 != 0:
            value += b'\x00'
    return value     



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


def aes_encrypt(data, key):
    cryptor = AES.new(key, AES.MODE_CBC, iv=b'0123456789abcdef')
    #將cut_value返回的32bytes的字元加密
    encrypt_aes = cryptor.encrypt(cut_value(data))
    #使用base64作encode後再轉為字串利儲存
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  
    return encrypted_text

def aes_decrypt(secret_str, key):
    cryptor = AES.new(key, AES.MODE_CBC, iv=b'0123456789abcdef')
    #使用base64作decoder返回
    base64_decrypted = base64.decodebytes(secret_str.encode(encoding='utf-8'))
    # 解密base64轉會的字元，並轉回str
    decrypted_text = str(cryptor.decrypt(base64_decrypted), encoding='utf-8')
    return decrypted_text



def token_bytes():
    nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)

def generate_key():

    key_path,result_path = read_control()

    nbytes = DEFAULT_ENTROPY
    key  = token_bytes()
  
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    with open(key_path,'wb+') as f:
        f.write(key)
    os.remove(result_path)
    return None


def get_key():
    key_path,result_path = read_control()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    if os.path.isfile(key_path):
        with open(key_path, 'rb+') as outfile:
            return outfile.read()
    
    else:
        generate_key()
        print('Can not find key, and system run function:generate_key automatic,please re run this process')
        exit()

