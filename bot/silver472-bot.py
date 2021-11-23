# -*- coding: utf-8 -*-

import telebot, logging, os
from consts import users
from tenacity import retry
from tenacity import wait_chain
from tenacity import wait_fixed

WORKDIR = "./"
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
# temporário | log para arquivo #
fh = logging.FileHandler('logs/debug.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %z')
fh.setFormatter(formatter)
telebot.logger.addHandler(fh)
# ----------------------------- #

API_TOKEN = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(API_TOKEN)
known_users = []

with open(os.path.join(WORKDIR, 'files/known_users.txt'), mode='r',encoding='utf-8') as f:
	for line in f:
		known_users.append(int(line.split("#")[0].strip()))

@bot.message_handler(commands=['start'])
def command_start(m):
	cid = m.chat.id
	if cid in known_users and m.chat.type == "private":
		bot.send_message(cid,"Seja bem vindo!")

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
	cid = m.chat.id
	if cid in known_users:
		with open(os.path.join(WORKDIR, 'files/help_file.txt'), 'r', encoding='utf-8') as help_file:
			help_text = help_file.read()
		bot.send_message(cid, help_text, parse_mode="Markdown")

@bot.message_handler(commands=['pikachu'])
def command_pikachu(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'upload_photo')
		bot.send_photo(cid,"AgADAQADeqgxG9ZaiEU6myK6BPNQjsp2DDAABH83Oz3z1ILBWZgFAAEC")

@bot.message_handler(commands=['zbetho'])
def command_zbetho(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'record_audio')
		bot.send_audio(cid,"CQADAQADWQAD1lqIRUGBFz-w2AGdAg")

@bot.message_handler(commands=['iutubi'])
def command_iutubi(m):
	cid = m.chat.id
	if cid in known_users:
		bot.forward_message(cid, users["silver"], 15)

@bot.message_handler(commands=['pqp'])
def command_pqp(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'record_audio')
		bot.forward_message(cid,users["silver"],18)
		bot.forward_message(cid,users["silver"],19)

@bot.message_handler(commands=['oibb'])
def command_oibb(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'record_audio')
		bot.send_voice(cid,"AwADBAADDAEAAhaglFPTHE39AW2hKgI")

@bot.message_handler(commands=['olokinho'])
def command_olokinho(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'record_audio')
		bot.send_voice(cid,"AwADBAADJAEAAq40XFI2NSjEdrThcAI")

@bot.message_handler(commands=['naruto'])
def command_naruto(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'record_audio')
		bot.send_voice(cid,"AwADBAADWwAD2tZMUF2yj_-0EK3YAg")

@bot.message_handler(commands=['rolinhamole'])
def command_rolinha(m):
	cid = m.chat.id
	if cid in known_users:
		bot.send_chat_action(cid,'upload_video')
		bot.send_message(cid,"Tá moli\n\nhttp://www.youtube.com/watch?v=Vc4xZ11ghnI")

################################### POLLING ###################################

@retry(wait=wait_chain(*[wait_fixed(10) for i in range(5)] +
						   [wait_fixed(20)]))
def polling_forever():
	bot.polling(none_stop=False, interval=0, timeout=20)

polling_forever()
