import time


class Performance:
    def __init__(self, message="", verbose=False):
        self.message = message
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000
        if self.verbose:
            print(f"{self.message} elapsed time: {self.msecs:.3f} ms")
