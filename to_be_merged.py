import sys


class MergedClass:
    def __init__(self, a, b):
        self.t = a
        self.tx = b
   


if __name__ == "__main__":
    mClass = MergedClass(sys.argv[0], sys.argv[1])
   