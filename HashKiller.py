from colorama import Fore, init
import hashlib
init()
print ('Starting...')

# USER DATA
userhash = input ("Input HASH : ")
userword = input ("Input PassList : ")
useralg = input ("Input Algorithm : ")

# brute
wordlist = open(userword,"r",encoding='utf-8')
for line in wordlist:
    hashpass = hashlib.new (useralg)
    hashpass.update (line.rstrip('\n').encode("utf-8"))
    if hashpass.hexdigest() == userhash:
         print (Fore.GREEN + "PassFound", line)
         break
    else:
        print (Fore.RED + "PassErr", line)
