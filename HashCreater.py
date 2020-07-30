from colorama import Fore, init
import hashlib
init()
print ('Starting...')

# USER DATA
userpass = input ("Input Pass : ")
useralg = input ("Input Algorithm : ")

hashpass = hashlib.new (useralg)
hashpass.update (userpass.encode("utf-8"))
print (Fore.GREEN + hashpass.hexdigest())
