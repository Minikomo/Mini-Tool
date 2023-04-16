import requests
import json
cookies = {
    '__dcfduid': 'a682e470dc6f11edb64507e8bccb6328',
    '__sdcfduid': 'a682e471dc6f11edb64507e8bccb63289feb0eee870f42e656a7c4e5896c26c76f1d063626f4cbde5d7efdd395aa03c6',
    '__cfruid': '1564700ab93b9deee5d22026b95dbaa2c60277fb-1681676382',
    'locale': 'en-US',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Mon+Apr+17+2023+00%3A12%3A02+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
}

headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'MTA4MTI1OTk1NTk3OTU3MTMxMA.G2FohF.SeAamhWDB1iJk1ZUTRgbGcyVUdqGcgAcBEpjkM',
    # 'cookie': '__dcfduid=a682e470dc6f11edb64507e8bccb6328; __sdcfduid=a682e471dc6f11edb64507e8bccb63289feb0eee870f42e656a7c4e5896c26c76f1d063626f4cbde5d7efdd395aa03c6; __cfruid=1564700ab93b9deee5d22026b95dbaa2c60277fb-1681676382; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Mon+Apr+17+2023+00%3A12%3A02+GMT%2B0200+(Mitteleurop%C3%A4ische+Sommerzeit)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
    'referer': 'https://discord.com/channels/190946039467868160/190946039467868160',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTExLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4OTYxNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
}

params = {
    'with_guild': 'false',
    'invite_code': 'gta',
}

response = requests.get(
    'https://discord.com/api/v9/guilds/190946039467868160/member-verification',

    cookies=cookies,
    headers=headers,
)
jsond = response.json()
jsond['form_fields'][0]['required'] = True
jsond['form_fields'][0]['response'] = True

print(jsond)

with open('thingss.txt','w') as f:
    f.write(str(jsond))