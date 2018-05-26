# -*- coding: utf-8 -*-

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
#from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler
from mmember_handler import MMemberHandler

import logging
import sys
import json

logging.basicConfig(
    filename='reduplicator1.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger('matrix_client.client')

# Global variables
USERNAME = "infobot"  # Bot's username
PASSWORD = ""  # Bot's password
SERVER = "https://localhost"  # Matrix server URL

with open('messages.json', 'r') as f:
    messages_raw = json.load(f)

messages = {
        'join': messages_raw['join']['message'] + '<p>\n' + ' '.join(['<strong>Q:</strong> '+o["Q"]+'<br />\n<strong>A:</strong> '+o["A"]+'<br />\n<br />\n' for o in messages_raw['join']['QA']]) + '</p>',
        'leave': messages_raw['leave']['message'],
        'ban': messages_raw['ban']['message']
}

#["invite", "join", "leave", "ban"]
def member_callback(room, event):
    print 'member call'
    print event
    if event['content']['membership'] == 'join' and 'prev_content' not in event and 'replaces_state' not in event and 'prev_content' not in event['unsigned'] and 'replaces_state' not in event['unsigned']:
        room.send_html('<a href=\"https://matrix.to/#/'+event['sender']+'\">'+event['content']['displayname']+'</a>: '+messages['join'].decode('utf-8'))
    if event['content']['membership'] == 'leave':
        room.send_text(messages['leave'])

def faq_callback(room, event):
    print 'faq call'
    room.send_html(messages['join'])

def main():
    # Create an instance of the MatrixBotAPI
    bot = MatrixBotAPI(USERNAME, PASSWORD, SERVER)

    member_handler = MMemberHandler(member_callback)
    bot.add_handler(member_handler)

    faq_handler = MCommandHandler("faq", faq_callback)
    bot.add_handler(faq_handler)

    faq1_handler = MCommandHandler("фаг", faq_callback)
    bot.add_handler(faq1_handler)

    bot.start_polling()

    while True:
        input()


if __name__ == "__main__":
    main()
