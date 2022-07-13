import random
from TrackCobra import User
from colorama import Style,Fore
R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
c = Fore.LIGHTMAGENTA_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
w = Fore.WHITE
y = Fore.LIGHTYELLOW_EX
print(b+f"""
  _____    _                                   ____ _               _             
 |_   _|__| | ___  __ _ _ __ __ _ _ __ ___    / ___| |__   ___  ___| | _____ _ __ 
   | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
   | |  __/ |  __/ (_| | | | (_| | | | | | | | |___| | | |  __/ (__|   <  __/ |   
   |_|\___|_|\___|\__, |_|  \__,_|_| |_| |_|  \____|_| |_|\___|\___|_|\_\___|_|   
                  |___/   {R}By fostn , Telegram Channel : https://t.me/ifostn
""")
print(G+'[1] p_t_p_t')
print(B+'[2] p_t_p')
print(Y+'[3] p_tp_p')

TheUser = input(w+'enter your choose : ')
def Check_1():

    thecount = int(input(w+"Enter The Count : "))
    c = "_"
    list = {'1','2','3','4','5','6','7','8','9','0','_'}
    a = 0
    valid = 0
    not_valid = 0
    user_index = {'1','2','3','4','5','6','7','8','9','0','.','-','_'}
    cc = {'_'}
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'

    while a < thecount:
        users = str("".join(random.choice(chars)for i in range(1)))
        users2 = str("".join(random.choice(chars)for i in range(1)))
        us = str(users+c+users2+c+users+c+users2)
        checker = User.Telegram(us)

        if checker == False and us[0] not in user_index and us[-1] not in cc  :
            print(G+"valid : "+ str(us))
            valid+=1
            with open('tle_valid.txt','a') as f:
                f.write(us+'\n')
        elif checker == True or us[0] in user_index or us[-1] in cc  :
            not_valid+=1
            print(R+"not valid : " + str(us))

        a =a +1
    print('-------------------------------')
    print(f"\r{G}valid [{valid}] {w}: {R}unvalid [{not_valid}] ",end="")

# Def 2
def Check_2():

    thecount = int(input(w+"Enter The Count : "))
    c = "_"
    list = {'1','2','3','4','5','6','7','8','9','0','_'}
    a = 0
    valid = 0
    not_valid = 0
    user_index = {'1','2','3','4','5','6','7','8','9','0','.','-','_'}
    cc = {'_'}
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'

    while a < thecount:
        users = str("".join(random.choice(chars)for i in range(1)))
        users2 = str("".join(random.choice(chars)for i in range(1)))
        us = str(users+c+users2+c+users)
        checker = User.Telegram(us)

        if checker == False and us[0] not in user_index and us[-1] not in cc  :
            print(G+"valid : "+ str(us))
            valid+=1
            with open('tle_valid.txt','a') as f:
                f.write(us+'\n')
        elif checker == True or us[0] in user_index or us[-1] in cc  :
            not_valid+=1
            print(R+"not valid : " + str(us))

        a =a +1
    print('-------------------------------')
    print(f"\r{G}valid [{valid}] {w}: {R}unvalid [{not_valid}] ",end="")
def Check_3():

    thecount = int(input(w+"Enter The Count : "))
    c = "_"
    list = {'1','2','3','4','5','6','7','8','9','0','_'}
    a = 0
    valid = 0
    not_valid = 0
    user_index = {'1','2','3','4','5','6','7','8','9','0','.','-','_'}
    cc = {'_'}
    chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'

    while a < thecount:
        users = str("".join(random.choice(chars)for i in range(1)))
        users2 = str("".join(random.choice(chars)for i in range(1)))
        us = str(users+c+users2+users+c+users2)
        checker = User.Telegram(us)

        if checker == False and us[0] not in user_index and us[-1] not in cc  :
            print(G+"valid : "+ str(us))
            valid+=1
            with open('tle_valid.txt','a') as f:
                f.write(us+'\n')
        elif checker == True or us[0] in user_index or us[-1] in cc  :
            not_valid+=1
            print(R+"not valid : " + str(us))

        a =a +1
    print('-------------------------------')
    print(f"\r{G}valid [{valid}] {w}: {R}unvalid [{not_valid}] ",end="")







if TheUser == "1":
    Check_1()
elif TheUser == '2':
    Check_2()
elif TheUser == '3':
    Check_3()
else:
    print(R+"Error choose")