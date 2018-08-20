from .flooder import Flooder
from .parsing import Parser

class App(Flooder, Parser):
    def __init__(self):
        self.preParse()
    
    def start(self, argv):
        self.parseArgs(argv=argv[1:])

