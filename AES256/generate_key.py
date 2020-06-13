import os
DEFAULT_ENTROPY = 32
#隨機產生key
def token_bytes():
    nbytes = DEFAULT_ENTROPY
    return os.urandom(nbytes)
#讀取control，取得key跟加密後的檔案的絕對路徑
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
#使用tokenbyte跟read_control獲取存檔位置及產生key，並且會移除原新的key及加密後的檔案
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