# AES256-Encryption-and-Decryption

# How to use?
Please follow these processes below:
1. Download this folder to your project folder.
2. Maintain Control.txt, and define path for key and encrypted connection information(encrype.config)
3. Run python generate_key.py, to get a new key.
4. Set conn,cursor = check_encrype('Any_string_you_define') in the code which you wanna connect DB.
## Important ! In Control.txt please be sure to keep the last string '\' in any path

# Introcution
### All you need is : conn,cursor = check_encrype('Any_string_you_define')
### For information security, please protect your key.key path

1. Please install : pycryptodome, and I suggest u using version-3.9.7

2. You must need to generate key first , use function : generate_key() (in en_decrype.py)

3. This project is assuming you need db connection, and protect all information.(you can modify by yourself)

4. How to use and reference sources are in the program, please check it.

### if any questions, please let me know.
