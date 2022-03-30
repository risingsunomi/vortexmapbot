"""
BotCmd class for bot command interface with twitter
Also archiving of last tweet to sqllite db to get the newest one
"""

import sqlite3
import os
import tweepy

class BotCmd:
    def __init__(self):
        self.sqldb = "local.sql"
        self.vortex_table = "vortexmap"
        self.twitter_consumer_key = os.getenv("TWITAPI")
        self.twitter_consumer_secret = os.getenv("TWITSEK")
        self.twitter_access_token_key = os.getenv("TWITAT")
        self.twitter_access_token_secret = os.getenv("TWITATS")
        self.twitter_api = None

        # create db table if not there
        try:
            self.sqlconn = sqlite3.connect(self.sqldb)
            self.sqlcur = self.sqlconn.cursor()

            self.sqlcur.execute(
                "SELECT count(name) FROM sqlite_master WHERE type='table' and name='{}'"
                .format(self.vortex_table)
            )

            if self.sqlcur.fetchone()[0] != 1:
                self.sqlcur.execute(
                    """
                    CREATE TABLE {}
                        (ID INT PRIMARY KEY NOT NULL,
                        USERNAME TEXT NOT NULL,
                        USERID INT NOT NULL,
                        POSTED DATETIME NOT NULL,
                        TWEET_TEXT LONGTEXT NOT NULL,
                        MAP_POINTS LONGTEXT NOT NULL,
                        CALCULATED_AT DATETIME DEFAULT CURRENT_TIMESTAMP
                        );
                    """.format(self.vortex_table))
        except Exception as err:
            raise err

    
    def connect_twitter(self):
        auth = tweepy.OAuthHandler(self.twitter_consumer_key, self.twitter_consumer_secret)
        auth.set_access_token(
            self.twitter_access_token_key,
            self.twitter_access_token_secret
        )

        self.twitter_api = tweepy.API(auth)

    def tweet(self, msg):
        if not self.twitter_api:
            self.connect_twitter()
        
        print(self.twitter_api.verify_credentials())
        if self.twitter_api.verify_credentials():
            self.twitter_api.update_status_with_media(status=msg, filename="7QSt.gif")