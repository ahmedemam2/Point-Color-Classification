import random


def sign(n):
    if n >= 0:
        return 1
    else:
        return -1


class Perceptron:
    weights = [0]*2
    lr = 0.1
    def __init__(self):
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(-1, 1)

    def guess(self,inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output
    def train(self,inputs,target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)): #tune weights
            self.weights[i] += error*inputs[i]*self.lr
