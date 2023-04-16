import requests
import base64
import urllib.parse

if mode == 4:
    Channel = tinput('Channel ID:')
    Message = tinput('Message ID:')
    emoji = urllib.parse.quote(tinput('Emoji'))


    with open('tokens.txt','r') as r:
        tokens = r.readlines
    for token in tokens:
        def cookies():
                    c = requests.get("https://discord.com")
                    return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "
        def xheaders():
                    xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
                    xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
                    return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))
        xconst, xprops = xheaders()
        headers = {
            "accept":               "*/*",
            "accept-encoding":      "gzip, deflate, br",
            "accept-language":      "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization":        token,
            "content-type":         "application/json",
            "cookie":               cookies(None),
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
            success(f'Token:{token[:10]}...   Reacted')
        else:
            error(f'Token:{token[:10]}...   Could not React')

