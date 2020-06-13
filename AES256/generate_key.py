import os
DEFAULT_ENTROPY = 32

def token_bytes():
    nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)

def read_control():
    with open(r'Control.txt',encoding='UTF-8-sig',mode='r') as config:
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

def generate_key():
    key_path,result_path = read_control()
    nbytes = DEFAULT_ENTROPY
    key  = token_bytes()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    with open(key_path,'wb+') as f:
        f.write(key)
    if os.path.exists(result_path):
        os.remove(result_path)
    return None

generate_key()
