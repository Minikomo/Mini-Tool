import requests
import base64	
def cookies():
                    c = requests.get("https://discord.com")
                    return f"__dcfduid={c.cookies['__dcfduid']}; __sdcfduid={c.cookies['__sdcfduid']}; "
def xheaders():
    xconst = '{"location":"Invite Button Embed","location_guild_id":null,"location_channel_id":"","location_channel_type":3,"location_message_id":""}'
    xprops = '{"os":"Windows","browser":"Discord Client","release_channel":"stable","client_version":"1.0.9006","os_version":"10.0.22000","os_arch":"x64","system_locale":"en-US","client_build_number":151638,"client_event_source":null}'
    return base64.b64encode(xconst.encode("utf-8")), base64.b64encode(xprops.encode("utf-8"))
serverid = input('funny')
def verify(token):
    xconst, xprops = xheaders()
    headers = {
            "accept":               "*/*",
            "accept-encoding":      "gzip, deflate, br",
            "accept-language":      "en-US,en-NL;q=0.9,en-GB;q=0.8",
            "authorization":        token,
            "content-type":         "application/json",
            "cookie":               cookies(),
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
    response = requests.get(f'https://discord.com/api/v9/guilds/{serverid}/member-verification',headers=headers,)
    return response.json()



json_data = {
    'version': '2020-12-29T12:44:18.702000+00:00',
    'form_fields': [
        {
            'field_type': 'TERMS',
            'label': 'Read and agree to the server rules',
            'values': [
                'Follow the Discord TOS and Community Guidelines',
                'Stay on-topic, no shitposting or advertising',
                'Respect people instead of cursing or bullying others',
                'Keep everything Safe For Work',
                'Use a simple nickname. Ideally the same as your Social Club username',
                'Respect administrative decisions',
                'Play Legit. Heist repeats are allowed. Stay away from any other forms of glitching or modding in online, including the discussion of online glitches / mods.',
                "Due to moderation, we're only able to support English, so please use that. You may DM or voice chat in other languages if people in the channel are already speaking that language.",
                'Assign yourself a platform role. Use `/role list` in any text channel to see how.',
            ],
            'required': True,
            'response': True,
        },
    ],
}

    

response = requests.put(
    'https://discord.com/api/v9/guilds/190946039467868160/requests/@me',
    headers=headers,
    json=json_data,
)
print(response.text)
print(response.status_code)
