from .flooder import Flooder

class App(Flooder):
    def __init__(self, args):
        singleArgs = args.split(" ", 4)
        account = singleArgs[1]
        times = singleArgs[2]
        title = singleArgs[3]
        message = singleArgs[4]
        self.floodAccount(
            account = account,
            times = int(times),
            comment = {
                "title": title,
                "content": message
            }
        )
