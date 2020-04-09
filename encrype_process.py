from en_decrype import *
import json
import os
'''
用法:僅須在程式中使用:
server_name ,user_id,password,db = check_encrype('db_name')
返回連線資訊，目前僅支援db連線
根據輸入的db字串(自訂並維護，如01編號代表某某DB)搜尋是否有加密資訊，若有則解密返回連線資訊；若無則啟動輸入資訊的流程，輸入完後會強制停止，請再重新執行一次程式
'''
def input_new_encrype(db_eng_name):
    print(f'Welcome to DB Connect in {db_eng_name}......')
    server_name = input('Please input server name:')
    user_id = input('Please input user id:')
    password = input('Please input password:')
    db = input('Please input db name:')
    with open('key.key','rb+') as f:
        key = f.read()
    server_encrype = aes_encrypt(server_name, key)
    user_encrype = aes_encrypt(user_id, key)
    password_encrype = aes_encrypt(password, key)
    db_encrype = aes_encrypt(db, key)
    store_encrype = dict()
    store_encrype['target_name'] = db_eng_name
    store_encrype['server_name'] = server_encrype
    store_encrype['user_id'] = user_encrype
    store_encrype['password'] = password_encrype
    store_encrype['db'] = db_encrype 
    with open('encrype.config', 'a') as outfile:
        json.dump(store_encrype, outfile)
        outfile.write('\n')
    print('Encrype Over, please re run process')
    exit()
    return None

def check_encrype(db_eng_name):
    if os.path.isfile('encrype.config'):
        pass
    else:      
        open("encrype.config","a")
    with open('encrype.config','r') as json_file:
        each_line = json_file.readlines()
        if len(each_line)!=0:
            for line in each_line:
                json_line = json.loads(line)
                if json_line['target_name'] ==db_eng_name:
                    key = get_key()
                    server_name = aes_decrypt(json_line['server_name'],key)
                    user_id = aes_decrypt(json_line['user_id'],key)
                    password = aes_decrypt(json_line['password'],key)
                    db = aes_decrypt(json_line['db'],key)
                    return server_name ,user_id,password,db
                else:
                    input_new_encrype(db_eng_name)              
        else:
            input_new_encrype(db_eng_name)
    return None


