import logging
import random
import time
from instagrapi import Client

class Bot:
    def __init__(self, username, password, logger):
        self.username = username
        self.password = password
        self.cl = Client()
        self.logger = logger
        self.account_info = dict()

    def login(self):
        try:
            self.cl.login(self.username, self.password)
            self.logger.set_log("Login Success")
            self.set_account_info()
        except Exception as e:
            self.logger.set_log(f"Login failed: {e}", level=logging.ERROR)
            raise

    def set_account_info(self):
        try:
            self.account_info = self.cl.account_info().model_dump()
        except Exception as e:
            self.logger.set_log(f"Failed to get account info: {e}", level=logging.ERROR)
            raise
        
    def get_account_info(self):
        return self.account_info

    def get_recent_media(self, username):
        user_id = self.cl.user_id_from_username(username)
        medias = self.cl.user_medias(user_id, 5)  
        return medias

    def post_media(self, media):
        caption = """
No problem! Here's the information about the Mercedes CLR GTR:

The Mercedes CLR GTR is a remarkable racing car celebrated for its outstanding performance and sleek design. Powered by a potent 6.0-liter V12 engine, it delivers over 600 horsepower.

Acceleration from 0 to 100 km/h takes approximately 3.7 seconds, with a remarkable top speed surprising 320 km/h.🥇

Incorporating adventure aerodynamic features and cutting-edge stability technologies, the CLR GTR ensures exceptional stability and control, particularly during high-speed maneuvers. 💨

Originally priced at around $1.5 million, the Mercedes CLR GTR is considered one of the most exclusive and prestigious racing cars ever produced. 💰

Its limited production run of just five units adds to its rarity, making it highly sought after by racing enthusiasts and collectors worldwide. 🌎
        """
        
        if media.media_type == 1:  # Photo
            self.cl.photo_upload(media.path, caption)
        elif media.media_type == 2:  # Video
            self.cl.video_upload(media.path, caption)
        elif media.media_type == 8:  # Album
            paths = [m.path for m in media.resources]
            self.cl.album_upload(paths, caption)
        self.logger.set_log(f"Posted media: {media.pk}", logging.INFO)

    def daily_post(self, target_accounts):
        selected_account = random.choice(target_accounts)
        self.logger.set_log(f"Selected account: {selected_account}", logging.INFO)
        recent_media = self.get_recent_media(selected_account)
        for media in recent_media:
            self.post_media(media)
            wait_time = random.randint(1800, 3600)
            self.logger.set_log(f"Waiting for {wait_time} seconds before next post.", logging.INFO)
            time.sleep(wait_time)
