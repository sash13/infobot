# -*- coding: utf-8 -*-

from matrix_bot_api.matrix_bot_api import MatrixBotAPI
#from matrix_bot_api.mregex_handler import MRegexHandler
from matrix_bot_api.mcommand_handler import MCommandHandler
from mmember_handler import MMemberHandler

import logging
import sys

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

messages = {
        'join': 'Привет, это Навальный. (на самом деле нет)<br />\n<br />\nНебольшой <strong>FAQ</strong>:<p>\n<strong>Q:</strong>Я зарегистрировался на matrix.org и мне пришло сообщение про какой-то GDPR и просят принять условия? Что делать?<br />\n<strong>A:</strong> Принимать условия, либо идти на другой сервер, список публичных серверов тут <a href="https://www.hello-matrix.net/public_servers.php">https://www.hello-matrix.net/public_servers.php</a> или попросить в этой конфе.<br />\n<br />\n<strong>Q:</strong> Почему у пользователей нет статусов онлайн/оффлайн?<br />\n<strong>A:</strong> Скорее всего ты зарегистрировался на матрикс.орге, у них отключена данная функция \"из-за нагрузок\". Выход есть, регистрироватся на другом публичном сервисе или попросить в этой конфе.<br />\n<br />\n<strong>Q:</strong> Зачем этот бот?<br />\n<strong>A: </strong>Одни участники конфы каждый раз когда приходит новый человек стараются объянить все, другие же бомбят от этого. Чтоб сохранить энергию первых и вторых был создан этот бот. Роботы должны работат, а люди творить и наслаждаться искусством (мемами)!<br />\n</p>',
'leave': 'https://www.youtube.com/watch?v=sos_GGtEQQQ',
'ban': 'https://www.youtube.com/watch?v=sos_GGtEQQQ'
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
