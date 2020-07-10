# AES256 Database Information Protection Project

## How to use it in your main code? It's so easy ! Just like example.py. All you need : conn,cursor = check_encrype('Any_string_you_define')

# 2020/07/10 Fix Log
1. fix bugs, please update if you cloned this project before 7/10.

# How to use?
Please follow these processes below when you first implememt:
1. Download folder AES256 to your project folder.
2. Please install : pycryptodome, and I suggest u using version-3.9.7
3. Maintain Control.txt, and define path for key and encrypted connection information.
4. Run generate_key.py, to get a new key.
5. conn,cursor = check_encrype('Any_string_you_define') -> in the code which you wanna connect DB.
### Important ! In Control.txt please be sure to keep the last backslash , like D:\test\AES256\
### I suggest you follow the same architecture like example.py.

# Introcution
1. This project focus on protecting server name,user id,password and db name by using AES256 encrype DB information.
2. You can define a connect string like TEST, and this program will ask you DB information corresponding to this TEST string, you need to key in  server name,user id,password and db name on command line once, then this program will encrype and it will decrypt automatically and connect to DB next time.
3. You can try it ! If any bug, please contact me for free.

### if any questions, please let me know.
