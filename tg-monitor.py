import configparser
import json
import re
import requests
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

class SetConfigParser(configparser.RawConfigParser):
    def get(self, section, option):
        val = configparser.RawConfigParser.get(self, section, option)
        return val.strip('"').strip("'")

config = SetConfigParser()

try:
    #config.read('/etc/eosmonitor/config.ini')
    config.read('config.ini')
except:
    pass


api_id = config.get("telegram", "api_id")
api_hash = config.get("telegram", "api_hash")
tg_username = config.get("telegram", "tg_username")
bpname = config.get("eosio", "bpname")
pushover_user_key = config.get("pushover", "pushover_user_key")
pushover_app_key = config.get("pushover", "pushover_app_key")
# Here you define the target channel that you want to listen to:
#user_input_channel = 'https://t.me/WAX_Mainnet_Aloha_Tracker'
user_input_channel = config.get("telegram", "user_input_channel")


def pushover(message,priority):
    # Set priority for message push
    if priority:
        priority = 1
    else:
        priority = 0
    try:
        r = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token": pushover_app_key,
        "user": pushover_user_key,
        "message": message,
        "priority": priority
        })
    except:
        print("Pushover message could not be send")


client = TelegramClient(tg_username, api_id, api_hash)

@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    # Get Message text
    newMessage = event.message.message

    bpFiltered = re.findall(bpname,newMessage)
    if len(bpFiltered) != 0:
        print("It has worked")
        pushover(newMessage,0)
    if len(bpFiltered) == 0:
        print("regex not working")

with client:
    client.run_until_disconnected()

