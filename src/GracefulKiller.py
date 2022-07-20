'''
Created on 20180208
Update on 20220720
@author: Eduardo Pagotto
'''

import signal
from Singleton import Singleton

class GracefulKiller(metaclass=Singleton):
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        self.kill_now = False

    def force_hand(self):
        self.kill_now = True

    def exit_gracefully(self,signum, frame):
        self.kill_now = True
