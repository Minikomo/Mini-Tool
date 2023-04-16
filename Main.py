import colorama
import os
import tls_client
import os
import base64
import requests
import threading
import random
from colorama import Fore
import datetime as dt
import time
import string
import discum
def info(message):
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.CYAN}INFO{Fore.RESET}] {Fore.LIGHTMAGENTA_EX}{message}{Fore.RESET}')
def error(message):
    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLACK_EX}{dt.datetime.fromtimestamp(time.time()).strftime(f"%H{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%M{Fore.LIGHTWHITE_EX}:{Fore.LIGHTBLACK_EX}%S")}{Fore.RESET}] [{Fore.RED}ERROR{Fore.RESET}] {Fore.RESET}{message}{Fore.RESET}')

def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')
def newl():
   print('\n')
def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def main():
    print(""" 
███▄ ▄███▓ ██▓ ███▄    █  ██▓   ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
▒██    ▒██ ░██░▓██▒  ▐▌██▒░██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
▒██▒   ░██▒░██░▒██░   ▓██░░██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░▓       ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░  ░      ░ ▒ ░░ ░░   ░ ▒░ ▒ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
░      ░    ▒ ░   ░   ░ ░  ▒ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
       ░    ░           ░  ░                  ░ ░      ░ ░      ░  ░      ░  
                                                                             """)
    newl()
    newl()
    print("""[1]Server Joiner             [2]Chanel Spammer""")
    newl()
    global mode
    mode = input('[?]Mode:')
if __name__ == "__main__":
    main()

if mode == '1':
    class Joiner:
        def __init__(self):
            os.system("cls")
            self.session = tls_client.Session(client_identifier="chrome_108")
            delay = input("[?]Delay:")
            invite_code = input("discord.gg/")
            with open("tokens.txt") as f:
                tokens = f.read().split('\n')
            ts = [threading.Thread(target=self.join,args=[token,invite_code,self.proxy()]) for token in tokens]
            for t in ts:
                time.sleep(int(delay))
                t.start()
            for t in ts:
                time.sleep(int(delay))
                t.join()
        
        def proxy(self):
            return None
        
        def join(self,token,invite,proxy):
            xconst, xprops = self.xheaders()
            headers = {
            "accept":               "*/*",
            "accept-encoding":      "gzip, deflate, br",
            "accept-language":      "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization":        token,
            "content-type":         "application/json",
            "cookie":               self.cookies(proxy),
            "origin":               "https://discord.com",
            "referer":              "https://discord.com/channels/@me/",
            "sec-fetch-dest":       "empty",
            "sec-fetch-mode":       "cors",
            "sec-fetch-site":       "same-origin",
            "user-agent":           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9006 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-context-properties": xconst.decode(),
            "x-debug-options":      "bugReporterEnabled",
            "x-discord-locale":     "en-US",
            "x-super-properties":   xprops.decode(),
        }
            req = self.session.post(f"https://discord.com/api/v9/invites/{invite}",json={},headers=headers)
            if req.status_code == 200:
                info('Server Joind with:'+token[:20]+'*************')
                with open('joined.txt','a') as c:
                    c.write(token+'\n')
                    c.close
            else:
                if 'captcha' in req.text:
                    error('Faild to join with:'+token[:20]+'*************     Reason:Captcha')
                else:
                    error('Faild to join with:'+token[:20]+'*************     Reason:Unkown')


        
        def cookies(self,proxy):
            c = requests.get("https://discord.com")
            return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "
        
        def xheaders(self):
            xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
            xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
            return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))

    Joiner()
if mode == '2':
    ID = input('[?] Chanel ID:')
    message = input('[?] Message:')
    massping = input('[?] Mass Ping(y/n):')
    def main(token):

        mem = open('members.txt','r').read().splitlines()
        while True:
            mem1 = random.choice(mem)
            mem2 = random.choice(mem)
            mem3 = random.choice(mem)
            mem4 = random.choice(mem)
            mem5 = random.choice(mem)
            mem6 = random.choice(mem)
            mem7 = random.choice(mem)
            mem8 = random.choice(mem)
            mem9 = random.choice(mem)
            mem10 = random.choice(mem)   
            time.sleep(0.5)
            url = f'https://discord.com/api/v9/channels/{ID}/messages'
            header = {"authorization": token}
            mess = " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            if massping == 'y':
                data = {"content": f"<@{mem1}> <@{mem2}> <@{mem3}> <@{mem4}> <@{mem5}> <@{mem6}> <@{mem7}> <@{mem8}> <@{mem9}>  {message}  {mess}"}
            else:
                data = {"content": f"{message}  {mess}"}
            r = requests.post(url, headers=header, data=data)
            print(r.text)
            if r.status_code == 200:
                print(token[:20]+'.....   typed message')
            elif r.status_code == 403:
                print(token[:20]+'.....  token banned')

    tokens = open('tokens.txt', 'r').read().splitlines()
    for token in tokens:
        print(token)
        t = threading.Thread(target=main, args=(token,))
        t.start()
if mode == '3':
    tukan = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
    guildd = input('[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
    chann = input('[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
    bot = discum.Client(token=tukan)

    def closefetching(resp,guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
            bot.gateway.close()

    def getmembers(guildid,channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
        bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)
    memberids = []

    for memberId in members:
        memberids.append(memberId)

    cls()

    with open('members.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')