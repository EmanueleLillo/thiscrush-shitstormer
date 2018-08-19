from requests import post

class PostRequest(object):
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload
    
    def resolve(self):
        self.request = post(self.url, data=self.payload)
        return self.request
    
    def getResponse(self):
        return self.request.text
