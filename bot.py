#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#pip3 install python-telegram-bot --upgrade


# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from env import TELEGRAM_TOKEN
from dobijecka import Dobijecka
import time


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hey, use /help for help')


def help(update, context):
	"""Send a message when the command /help is issued."""
	update.message.reply_text('Help!\n/last - date of last event')


def last(update, context):
	update.message.reply_text('Fetching, please wait...')
	success, data = dobijecka.is_dobijecka()
	
	if success != None:
		is_today = success
		date = data['date']
		start = data['start']
		stop = data['stop']
		msg = data['msg']

		update.message.reply_text('%s, from %s, to %s' % (date, start, stop))
		if is_today:
			update.message.reply_text('Dnes je dobíječka!, msg: %s' % msg)
		else:
			update.message.reply_text('not today')

	else:
		update.message.reply_text('failed! reason: %s' % data['error'])


def echo(update, context):
	"""Echo the user message."""
	update.message.reply_text(update.message.text)



def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
	dobijecka = Dobijecka()

	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(TELEGRAM_TOKEN, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler("last", last))

	# on noncommand i.e message - echo the message on Telegram
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.

	try:
		while True:

			time.sleep(10)

	except KeyboardInterrupt:
		print('KeyboardInterrupt')

	print('stopping')
	updater.stop()
	#updater.idle()