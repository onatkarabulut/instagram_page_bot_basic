from Bot.bot import Bot
from Log.logger import Logger
from Config.config import USERNAME, PASSWORD, TARGET_ACCOUNTS
import schedule
import time
import random

def run_post(bot_instance):
    bot_instance.daily_post(TARGET_ACCOUNTS)

def schedule_random_post(bot_instance):

    hours = random.randint(1, 3)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    interval = hours * 3600 + minutes * 60 + seconds

    schedule.every(interval).seconds.do(run_post, bot_instance=bot_instance)
    print(f"Scheduled next post in {hours} hours, {minutes} minutes, and {seconds} seconds.")

if __name__ == '__main__':
    logger = Logger()
    bot = Bot(USERNAME, PASSWORD, logger)
    bot.login()

    run_post(bot)
    schedule_random_post(bot)

    while True:
        schedule.run_pending()
        time.sleep(1)
