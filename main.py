from Bot.bot import Bot
from Log.logger import Logger
from Config.config import USERNAME, PASSWORD, TARGET_ACCOUNTS
import time
import random
import logging

def run_daily_post(bot_instance, target_accounts):
    while True:
        selected_account = random.choice(target_accounts)
        bot_instance.logger.set_log(f"Selected account: {selected_account}", logging.INFO)
        recent_media = bot_instance.get_recent_media(selected_account)
        
        for media in recent_media:
            bot_instance.post_media(media)
            sleep_time = random.randint(1800, 3600)  
            bot_instance.logger.set_log(f"Sleeping for {sleep_time} seconds", logging.INFO)
            time.sleep(sleep_time)

if __name__ == '__main__':
    logger = Logger()
    bot = Bot(USERNAME, PASSWORD, logger)
    bot.login()

    run_daily_post(bot, TARGET_ACCOUNTS)
