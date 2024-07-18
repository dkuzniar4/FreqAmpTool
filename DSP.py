import math


class LowPassSinglePole:
    def __init__(self):
        pass
    def reset(self):
        self.y = 0
    def filter(self, x):
        self.y += self.b * (x - self.y)
        return self.y
    def setParam(self, freqCut, fs):
        freqCut /= fs
        decay = math.exp(-2 * math.pi * freqCut)
        self.b = 1 - decay
        self.reset()
