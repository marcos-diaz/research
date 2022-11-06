from math import sqrt, floor
from random import random, uniform
from types import SimpleNamespace
import numpy as np

class Montecarlo:
    def __init__(self, iterations):
        self.iterations = iterations

    def run(self, variables, function):
        avg_bucket = np.zeros(self.iterations)
        for i in range(self.iterations):
            if not i % (self.iterations / 40):
                print('#', end='', flush=True)
            args = [x() for x in variables]
            result = function(*args)
            avg_bucket[i] = result
        avg = np.average(avg_bucket)
        print()
        return avg

    def run_data(self, data, variables, function):
        avg_bucket = []
        for i in range(self.iterations):
            if not i % (self.iterations / 40):
                print('#', end='', flush=True)
            args = [x() for x in variables]
            result = function(*args)
            avg_bucket.append(result)
            x = int((floor(abs(args[0]) * len(data.x))))
            if data.z is None:
                data.y[x] += result
            else:
                y = int((floor(abs(args[1]) * len(data.y))))
                data.z[x][y] += result
        data.avg = sum(avg_bucket) / self.iterations
        print(' ', data.avg)
        return data
