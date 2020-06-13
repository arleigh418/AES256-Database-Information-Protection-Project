from Crypto.Cipher import AES
import os
import hashlib
import base64
import json
from en_decrype import *
import pandas as pd

DEFAULT_ENTROPY = 32
#讀取control，取得key跟加密後的檔案的絕對路徑
def read_control_txt():
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
#獲取key
def get_key_txt():
    key_path,result_path = read_control_txt()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    if os.path.isfile(key_path):
        with open(key_path, 'rb+') as outfile:
            return outfile.read()
    #如果沒找到key，則會自動幫產，並告訴你此次流程並未繼續，因為連key都找不到
    else:
        generate_key()
        print('Can not find key, and system run function:generate_key automatic,please re run this process')
        exit()

#取解密的原程式中的片段，來對目標加密後的檔案作解密確認，併獲取連線字串對應的Server及User id
def get_info():
    key_path,result_path = read_control_txt()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    conn_name = []
    server_name = []
    user_id = []
    if os.path.isfile(result_path):
        pass
    else:      
        print('找不到已加密的檔案，請確認')
        exit()
    with open(result_path,'r') as json_file:
        each_line = json_file.readlines()
        json_file.close()
        if len(each_line)!=0:
            for line in each_line:
                json_line = json.loads(line)
                key = get_key_txt()
                print('連線字串:',json_line['target_name'])
                print('對應的Server:',str(aes_decrypt(json_line['server_name'],key)))
                print('使用的User id:',str(aes_decrypt(json_line['user_id'],key)))
                print('=================================================')
    

get_info()        