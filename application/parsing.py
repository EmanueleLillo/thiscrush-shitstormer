from argparse import ArgumentParser

class Parser(object):
    def preParse(self):
        self.parser = ArgumentParser(
            prog="thiscrush-storm",
            description="Thiscrush Shitstormer written in Python by Emanuele Lillo."
        )
        self.parser.add_argument(
            "username", help="User's Account."
        )
        self.parser.add_argument(
            "-c", "--count", default=5, help="Requests per Thread. (RPT)", type=int, metavar="COUNT PER THREAD"
        )
        self.parser.add_argument(
            "-t", "--threads", default=1, help="Thread count.", type=int
        )
        self.parser.add_argument(
            "-n", "--title", default="Opz", help="Title of the message."
        )
        self.parser.add_argument(
            "-m", "--message", default="You got Hacked.", help="The message itself."
        )

    def parseArgs(self, argv):
        args = self.parser.parse_args(argv)
        
        print("Username: ", end="")
        if not args.username:
            print("required!")
            return 0
        self.account = args.username
        print(self.account)

        print("RPT: ", end="")
        self.times = args.count
        print(self.times)
        
        print("Threads Count: ", end="")
        self.threads = args.threads
        print(self.threads)
        
        print("Title: ", end="")
        self.title = args.title
        print("OK")

        print("Message: ", end="")
        self.message = args.message
        print("OK")

        self.floodAccount()

        