# AES256-Encryption-and-Decryption

# How to use?
Please follow these processes below when you first implememt:
1. Download folder AES256 to your project folder.
2. Please install : pycryptodome, and I suggest u using version-3.9.7
3. Maintain Control.txt, and define path for key and encrypted connection information.
4. Run generate_key.py, to get a new key.
5. conn,cursor = check_encrype('Any_string_you_define') _in the code which you wanna connect DB.
### Important ! In Control.txt please be sure to keep the last backslash , like D:\test\AES256\

# Introcution
1. This project focus on protect server name,user id,password and db name by using AES256 encrype DB information.
2. You can define a connect string like TEST, and this program will ask you DB information corresponding to this TEST string, you need to key in  server name,user id,password and db name on command line once, then this program will encrype and it will decrypt automatically and connect to DB next time.
3. You can try it ! If any bug, please contact me for free.

### if any questions, please let me know.
