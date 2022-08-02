import time, webbrowser, os, sys, random, string, urllib
from random import choice
from urllib.request import urlopen
def url_open():
    url = str(input('Enter the URL: '))
    browser = input('Whats your default browser?: ')
    os.system('TASKKILL /F /IM ' + browser + 
    ".exe")
    webbrowser.open(url)
    print('Success')
    main()
def name_gen():
    def random_name_generator(first, second, x):
        names = []
        for i in range(x):
            names.append("{0} {1}".format(choice(first), choice(second)))
        return set(names)
    cont = input('what continent are you from?: ')
    if cont.capitalize() == 'Europe':
        first_names = ["Abella", "Mia", "Landon",
            "Logan", "Kennedy", "Tom", "Avery"]
        last_names = ["Silva", "Garcia", "Martin",  
            "Murphy", "Smith", "Hansen", "Johansson","Korhonen","Jensen",
            "De Jong"]
    elif cont.capitalize() == 'North America':
        first_names = ["Sophia",
              "Isabella","Emma","Olivia","Jacob",
              "Mason","William","Jayden"]
        last_names = ["Johnson",
               "Miller", "Jones",
                "Murphy", "Smith", "Williams", "Anderson"]
    elif cont.capitalize() == 'Asia':
        first_names = ["Ryder","Abdullah","Abdul","Kim"
               ,"Aran","Cai","Va","Arjun"]
        last_names = ["Wang","Li","Zhang","Liu","Chen",
               "Yang","Huamg","Zhao"]
    elif cont.capitalize() == ['South America',
             'Antartica', 'Middle East','Africa']:
        first_names = ["Liam","Noah","Oliver",
             "William","Elijah","James","Benjamin","Lucas","Mason","Ethan"]
        last_names = ["Johnson", "Miller",
            "Jones", "Murphy", "Smith",
            "Williams", "Anderson", "Brown",
            "Davis","Garcia"]
    else:
        first_names = ["Liam","Noah","Oliver",
                "William","Elijah","James","Benjamin","Lucas","Mason","Ethan"]
        last_names = ["Johnson", "Miller",
               "Jones", "Murphy", "Smith",
              "Williams", "Anderson", "Brown",
              "Davis","Garcia"]
    names = random_name_generator(first_names, last_names, 5)
    print('\n'.join(names))
    main()
def pass_gen():
    chars = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKL
    MNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'''
    number = int(1)
    length = int(input('password length?'))
    print('\nhere is your passwords:')
    for pwd in range(number): 
        password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    main()
def pass_check():
    def pass1():
            invalidcharacters = set(string.punctuation)
            while True:
                password = input('Whats the Password \n')
                if len(password) <= 7 :
                    print('Your Password is to short')
                else :
                    if (any(x.isdigit() for 
                    x in password)) and (any(x.islower()
                        for x in 
                        password)) and any(char in invalidcharacters for 
                        char in
                         password) and (any(x.isupper() for x in password)):
                        print('Good! You have created a strong password ')
                        break
                    else:
                        print('''Please enter Atleast, an upper case , 
                        lowercase , special character !@#$%^&*()? and digit''')
    pass1()
    main()
def email_gen():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    amount = int(1)
    length = 7
    end = '@gmail.com'
    if amount == 1:
        print('\nhere is your email:')
    for x in range(amount): 
        email = ''
    for c in range(length):
        email += random.choice(chars)
    emails = email+end
    print(emails)
    main()
def speed_wifi():
    def is_internet():
        try:
            urlopen('https://www.google.com/', timeout=1)
            return True
        except urllib.error.URLError as Error:
            print(Error)
        return False
    if is_internet():
        print()
        print("Internet is up")
        print()
    else:
        print()
        print("Internet is down")
        print() 
    main()
def main():
    print('1: Url Opener')
    print('2: Name Generator')
    print('3: Password Generator')
    print('4: Password Checker')
    print('5: Email generator')
    print('6: Wifi Checker')
    print('7: All of them')
    print('8: End Program')
    y = str(input('What do you want to run?: '))
    if y == '1':
        url_open()
    if y == '2':
        name_gen()
    if y == '3':
        pass_gen()
    if y == '4':
        pass_check()
    if y == '5':
        email_gen()
    if y == '6':
        speed_wifi()
    if y == '7':
        all_them()
    if y == '8':
        print('''████░██░██░░▄███▄░░██▄░██░██░▄██''')
        print('''░██░░██▄██░██▀░▀██░███▄██░████▀░''')
        print('''░██░░██▀██░███████░██▀███░████▄░''')
        print('''░██░░██░██░██░░░██░██░░██░██░▀██''')
        print(''' \ \   / /         
                   \ \_/ /__  _   _ 
                    \   / _ \| | | |
                     | | (_) | |_| |
                     |_|\___/ \__,_|''')
        sys.exit()
main()