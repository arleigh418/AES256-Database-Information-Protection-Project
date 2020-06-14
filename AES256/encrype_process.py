from AES256.en_decrype import *
import json
import os
import pymssql
'''
用法:僅須在程式中使用:
conn,cursor = check_encrype('Any_string_you_define')
'''
def input_new_encrype(db_eng_name):
    print(f'Welcome to DB Connect in {db_eng_name}......')
    server_name = input('Please input server name:')
    user_id = input('Please input user id:')
    password = input('Please input password:')
    db = input('Please input db name:')
    try:
        pymssql.connect(server=server_name ,user = user_id ,password = password ,database = db)
    except:
        print('**********Error on connect sql, please check your information**********')
        exit()
    
   
    key_path,result_path = read_control()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    key = get_key()
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
 
    with open(result_path, 'a') as outfile:
        json.dump(store_encrype, outfile)
        outfile.write('\n')
    outfile.close()
   
    print('Encrype Over !')
    exit()
    return None

def check_encrype(db_eng_name):
    status = 0
    key_path,result_path = read_control()
    key_path = (key_path+'key.key').replace('\n','')
    result_path = (result_path+'encrype.config').replace('\n','')
    if os.path.isfile(result_path):
        pass
    else:      
        open(result_path,"a")
    with open(result_path,'r') as json_file:
        each_line = json_file.readlines()
        json_file.close()
        if len(each_line)!=0:
            for line in each_line:
                json_line = json.loads(line)

                if json_line['target_name'] ==db_eng_name:  
                    status+=1
                    key = get_key()
                    server_name = aes_decrypt(json_line['server_name'],key)
                    user_id = aes_decrypt(json_line['user_id'],key)
                    password = aes_decrypt(json_line['password'],key)
                    db = aes_decrypt(json_line['db'],key)
                    try:
                        conn = pymssql.connect(server=server_name ,user = user_id ,password = password ,database = db)
                        cursor = conn.cursor()                    
                    except:
                        print('Descrpt success , but sql connect error.Please check if userid or password are motified')
                        exit()

            if status ==0:
                input_new_encrype(db_eng_name)              
        else:
            input_new_encrype(db_eng_name)
    return conn,cursor
