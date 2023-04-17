import random
import colorama
import requests
import tls_client
from colorama import Fore, Style
import string
import discum
import threading
import datetime
from datetime import datetime
import json
import time
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
import easygui, os
from art import tprint
import re
import base64
import urllib.parse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

import ctypes


colorama.init()
debugmode = False

def title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def error(message):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.RED}[ERROR]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def warning(message):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.YELLOW}[WARN]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def debug(message):
    if debugmode:
        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTYELLOW_EX}[DEBUG]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def solver(message):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.MAGENTA}[SOLVER]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def success(message):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.GREEN}[SUCCESS]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def tinput(message):
    r = input(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.LIGHTCYAN_EX}[INPUT]{Style.RESET_ALL} [{threading.current_thread().name.strip(' (<lambda>), ''').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}{Fore.LIGHTBLACK_EX} >>> {Style.RESET_ALL}")
    return r


def info(message):
    print(
        f"[{datetime.now().strftime('%H:%M:%S')}] {Fore.BLUE}[INFO]{Style.RESET_ALL} [{threading.current_thread().name.replace(' (<lambda>)', '').replace('-', ' ').replace('MainThread', 'Main Thread').replace('MainThre', 'Main Thread').replace('(start', '').replace('(start)', '')}] {message}{Style.RESET_ALL}")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def hackerspeak(text):
    leet_dict = {
        'a': ['4', '@'],
        'A': ['4', '@'],
        'e': ['3', '€'],
        'E': ['3', '€'],
        'i': ['1', '!'],
        'I': ['1', '!'],
        'o': ['0', '¤'],
        'O': ['0', '¤'],
        't': ['7', '+'],
        'T': ['7', '+'],
        's': ['5', '$'],
        'S': ['5', '$'],
        'l': ['1', '|'],
        'L': ['1', '|'],
        'b': ['8', 'ß'],
        'B': ['8', 'ß'],
        'g': ['9', '6'],
        'G': ['9', '6'],
        'z': ['2', '7'],
        'Z': ['2', '7']
    }

    leet_text = ''.join([random.choice(leet_dict.get(char, [char])) for char in text])

    return leet_text


def uwuspeak(text):
    def add_emoticon(match):
        emoticons = ['OwO', 'UwU', '^w^', '>w<', '>wO', 'ÓwÒ', 'ÒwÓ', 'òωó', 'ÓωÒ', '(・`ω´・)', '(U・x・U)']
        return f'{match.group(0)} {random.choice(emoticons)}'

    def get_emoticon():
        emoticons = ['OwO', 'UwU', '^w^', '>w<', '>wO', 'ÓwÒ', 'ÒwÓ', 'òωó', 'ÓωÒ', '(・`ω´・)', '(U・x・U)']
        return random.choice(emoticons)

    text = re.sub(r'[Ll]', 'W', text)
    text = re.sub(r'[Rr]', 'W', text)
    text = re.sub(r'[Nn]', 'Ny', text)
    text = re.sub(r'\bth', 'd', text)
    text = re.sub(r'\bTh', 'D', text)
    text = re.sub(r'(?<![.!])\B[!?.]\B', add_emoticon, text)
    text = re.sub(r'\.{3}', '... UwU', text)

    text = f'{get_emoticon()} {text} {get_emoticon()}'

    return text


def main():
    tprint('Mini-Tools','3-d')
    print()
    print("""[1] Server Joiner             [2] Channel Spammer           [3] ID Scraper""")
    print("""[4] Message Reactor           [5] Discord verify            [6] Channel Scraper""")
    print()
    global mode
    mode = tinput('Mode')


if __name__ == "__main__":
    main()

if mode == '1':
    class Joiner:
        def __init__(self):
            os.system("cls")
            self.session = tls_client.Session(client_identifier="chrome_108")
            invite_code = tinput("Invite code").replace("https://discord.gg/", '')
            delay = tinput("Delay")
            with open("tokens.txt") as f:
                tokens = f.read().split('\n')
            ts = [threading.Thread(target=self.join, args=[token, invite_code, self.proxy()]) for token in tokens]
            for t in ts:
                time.sleep(int(delay))
                t.start()
            for t in ts:
                time.sleep(int(delay))
                t.join()

        def proxy(self):
            return None

        def join(self, token, invite, proxy):
            xconst, xprops = self.xheaders()
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en-NL;q=0.9,en-GB;q=0.8",
                "authorization": token,
                "content-type": "application/json",
                "cookie": self.cookies(proxy),
                "origin": "https://discord.com",
                "referer": "https://discord.com/channels/@me/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9012 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
                "x-context-properties": xconst.decode(),
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": xprops.decode(),
            }
            req = self.session.post(f"https://discord.com/api/v9/invites/{invite}", json={}, headers=headers)
            if req.status_code == 200:
                success(f'Joined! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}')
                with open('joined.txt', 'a') as c:
                    c.write(token + '\n')
                    c.close
            else:
                if 'captcha' in req.text:
                    error(f'Failed to join! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}(Captcha)')
                else:
                    error(f'Failed to join! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}({req.json()})')

        def cookies(self, proxy):
            c = requests.get("https://discord.com")
            return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "

        def xheaders(self):
            xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
            xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
            return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))


    Joiner()
if mode == '2':
    ID = tinput('Channel IDs (Seperated by commas)').strip(' ').split(',')
    messages = tinput('Messages (Seperated by commas)').split(',')
    massping = tinput('Mass Ping (y/n)')
    delay = tinput('Delay:')
    
    if massping == 'y':
        pingcount = tinput("How many pings per message?")
    x = tinput("Should we modify the text? (y/n)")
    if x == 'y':
        e = tinput("How should we modify it? (1. uwuspeak 2. 1337 (leet) speak)")
        
        if e == '1':
            def messagernd():
                return uwuspeak(random.choice(messages))
        elif e == '2':
            def messagernd():
                return hackerspeak(random.choice(messages))
        else:
            
            warning("Invalid input! Not modifying message.")
    else:
        def messagernd():
            return random.choice(messages)

    def main(token):

        mem = open('members.txt', 'r').read().splitlines()
        while True:
            channel = random.choice(ID)
            print(channel)
            # with open('big.txt','r')as f:
            #     lines = f.readlines()
            with open('big.txt','r')as ff:
                big = ff.readlines()
            

            time.sleep(0.5)
            url = f'https://discord.com/api/v9/channels/{channel}/messages'
            header = {"authorization": token}
            mess = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            if massping == 'y':
                mem1 = [f"<@{random.choice(mem)}>" for _ in range(int(pingcount))]
                mems = ' '.join(mem1)
                data = {"content": f"{random.choice(big)} | {mems} {mess}"}
            else:
                data = {"content": f" {random.choice(big)}  {mess}"}
            r = requests.post(url, headers=header, data=data)

            if r.status_code == 200:
                success(f'Sent message! | {token[:20]}***************')
            elif r.status_code == 403:
                error(f'Failed to send message! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}(Locked Token)')
            elif 'rate' in r.text.lower():
                warning(f'Failed to send message! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}(Ratelimited)')
            else:
                error(f'Failed to send message! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}({r.json()})')
            time.sleep(int(delay))

    tokens = open('tokens.txt', 'r').read().splitlines()
    for token in tokens:
        t = threading.Thread(target=main, args=(token,))
        t.start()

if mode == '3':
    tukan = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
    guildd = input('[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
    chann = input('[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
    bot = discum.Client(token=tukan)


    def closefetching(resp, guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function': closefetching, 'params': {'guildid': guildid}})
            bot.gateway.close()


    def getmembers(guildid, channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all', wait=1)
        bot.gateway.command({'function': closefetching, 'params': {'guildid': guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members


    members = getmembers(guildd, chann)
    memberids = []

    for memberId in members:
        memberids.append(memberId)

    cls()

    with open('members.txt', 'w') as ids:
        for element in memberids:
            ids.write(element + '\n')


if mode == '16':
    tokenlist = open(easygui.fileopenbox(), 'r').read().splitlines()
    channel = int(tinput("Channel ID"))
    server = int(tinput("Server ID"))
    deaf = tinput("Deafen: (y/n)")
    if deaf == "y":
        deaf = True
    if deaf == "n":
        deaf = False
    mute = input("Mute: (y/n)")
    if mute == "y":
        mute = True
    if mute == "n":
        mute = False
    stream = input("Stream: (y/n)")
    if stream == "y":
        stream = True
    if stream == "n":
        stream = False
    video = input("Video: (y/n)")
    if video == "y":
        video = True
    if video == "n":
        video = False
    threads = int(tinput("Threads"))
    executor = ThreadPoolExecutor(max_workers=int(threads))

    def run(token):
        while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = json.loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(json.dumps({"op": 2, "d": {"token": token, "properties": {"$os": "windows", "$browser": "Discord",
                                                                              "$device": "desktop"}}}))
            ws.send(json.dumps({"op": 4,
                                "d": {"guild_id": server, "channel_id": channel, "self_mute": mute, "self_deaf": deaf,
                                      "self_stream?": stream, "self_video": video}}))
            ws.send(json.dumps({"op": 18, "d": {"type": "guild", "guild_id": server, "channel_id": channel,
                                                "preferred_region": "singapore"}}))
            ws.send(json.dumps({"op": 1, "d": None}))
            ws.close()
            time.sleep(0.1)


    title(f"Mini-Tool | Total Tokens: {len(tokenlist)}")
    i = 0
    for token in tokenlist:
        executor.submit(run, token)
    i += 1
    success("Joined voice channel!")
    time.sleep(0.01)

if mode == '4':
    Channel = tinput('Channel ID')
    Message = tinput('Message ID')
    emo = tinput('Emoji')
    emoji = urllib.parse.quote(emo)
    with open("joined.txt") as f:
        tokens = f.readlines()


    def main(token):
        def cookies():
            c = requests.get("https://discord.com")
            return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "

        def xheaders():
            xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
            xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
            return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))

        xconst, xprops = xheaders()
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization": token,
            "content-type": "application/json",
            "cookie": cookies(),
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9006 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-context-properties": xconst.decode(),
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": xprops.decode(),
        }

        params = {
            'location': 'Message',
            'type': '0',
        }

        response = requests.put(
            f'https://discord.com/api/v9/channels/{Channel}/messages/{Message}/reactions/{emoji}/%40me',
            params=params,
            headers=headers,
        )
        if response.status_code == 204:
            success(f'Token:{token[:10]}...     Reacted')
        else:
            error(f'Token:{token[:10]}...     Could not React')


    for token in tokens:
        threading.Thread(target=main, args=(token.strip('\n'),)).start()

if mode == '5':
    serverid = tinput('Server id:')
    with open("joined.txt") as f:
        tokens = f.readlines()

    def cookies():
        c = requests.get("https://discord.com")
        return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "


    def xheaders():
        xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
        xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
        return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))


    def verify(token):
        xconst, xprops = xheaders()
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization": token,
            "content-type": "application/json",
            "cookie": cookies(),
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9006 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-context-properties": xconst.decode(),
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-super-properties": xprops.decode(),
        }
        jasuoon = requests.get(f'https://discord.com/api/v9/guilds/{serverid}/member-verification', headers=headers, )
        json_data = jasuoon.json()
        json_data['form_fields'][0]['required'] = True
        json_data['form_fields'][0]['response'] = True
        verify = requests.put(f'https://discord.com/api/v9/guilds/{serverid}/requests/@me', headers=headers,
                              json=json_data, )
        if verify.status_code == 201:
            success(f'Verified! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}')
        elif verify.status_code == 403:
            error(f'Failed to verify! | {token[:20]}*************** {Fore.LIGHTBLACK_EX}(Locked Token)')
        else:
            error(f'Token:{token}...   Could not verify')


    for token in tokens:
        threading.Thread(target=verify, args=(token.strip('\n'),)).start()

if mode == '6':
    token = tinput('Token:')
    server = tinput('Server ID:')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://discord.com/login')



    info('Logging into discord')
    wait = WebDriverWait(driver, 10) 
    element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div/div/div/form/div[2]/div/div[1]')))

    driver.execute_script(f"""
    function login(token) {{
        setInterval(() => {{
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"{token}"`
        }}, 50);
        setTimeout(() => {{
        location.reload();
        }}, 2500);
    }}
    login("{token}");
    """)


    time.sleep(7)
    success('Logged into Discord')
    driver.get(f'https://discord.com/channels/{server}/')
    driver.execute_script("document.body.style.zoom = '4%';")
    time.sleep(8)
    
    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
    with open('webpage.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
        links = re.findall(r'channels___\d{18,21}', html_content)
    info('Saved html')
    
    ids = []
    for link in links:
        
        id = re.search(r'\d{18,21}', link).group()
        success(f'Found ID:{id}')
        ids.append(id)
    valid = []
    print('Checking IDs if Valid')
    for number in ids:
        check = requests.post(f'https://discord.com/api/v9/channels/{number}/messages',data={'content': ' '},headers={"authorization": token})
        if '50006' in check.text:
            success(f'ID:{number} Is a Text Channel')
            valid.append(number)
            with open('Channels.txt','a')as g:
                g.write(number + '\n')
        elif '50008' in check.text:
            warning(f'ID:{number} Is not a Text Channel')
        elif '50013'in check.text:
            warning(f'ID:{number} Missing Permissions')
        else:
            error(f'ID:{number} Does not exitst'  + check.text)
    valid_str = str(valid)
    valid2 = valid_str.strip('[').strip(']').replace("'",'')
    print(valid2)   