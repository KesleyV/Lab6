import sys
import os

class ProgressBar:
    def __init__(self, prefix, maximum = 0):
        self.maximum = maximum
        self.prefix = prefix
        self.count = 0

    def add(self, value):
        self.count+=value
        self.update()

    def update(self):
        if(self.maximum > 0):
            value = (float(self.count)/float(self.maximum)) * 100
            percentage = int(value)
            left = 100 - percentage
            print("%s: [%s%s] %i/%i(%i%%)\r" % (self.prefix, "#"*percentage, "."*left, self.count, self.maximum, percentage))

    def close(self):
        os.system('cls' if os.name == 'nt' else 'clear')