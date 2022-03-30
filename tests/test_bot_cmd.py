"""
Test bot commands
"""

import unittest
from bot_cmd import BotCmd

class TestBotCmd(unittest.TestCase):
    def test_one(self):
        # send a test tweet
        bot = BotCmd()
        bot.tweet("testing!")

if __name__ == "__main__":
    unittest.main()