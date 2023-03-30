import time
import os

import telebot

BOT_TOKEN = os.environ['BOT_TOKEN']

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='markdown')


help_msg = """Howdy, this is a bot that can notify you via TG when your slurm job finishes on certain clusters.

Below are steps to use this bot.

1. Send `/getcid` to this bot, and get your unique CID
2. Run `snotified.sh <CID>` on head node of the cluster (maybe use a tmux session to keep it always online)
3. Use `srun` with argument `--mail-type=END` (see more in `man srun`) to get notified for this job.
"""

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    print('[{}] Recv msg: {} {}'.format(time.time(), message.chat.id, message.chat.username))
    bot.reply_to(message, help_msg)


@bot.message_handler(commands=['getcid'])
def bind_user(message):
    cid = message.chat.id
    print('[{}] Recv cid: {} {}'.format(time.time(), message.chat.id, message.chat.username))
    bot.reply_to(message, 'Please remember your cid: `{}`'.format(cid))


bot.polling()
