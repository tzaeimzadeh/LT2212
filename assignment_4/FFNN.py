import numpy as np
import math

#https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
class neuralNetwork:
    def __init__(self, x, y, b, c, N, M):
        self.input = x
        self.b = 1
        self.c = 1
        self.N = N
        self.M = M
        self.weight1 = np.random.rand(self.input.shape[1], N)
        self.weight2 = np.random.rand(N, M)
        self.y = y
        self.output = np.zeros(y.shape)

    def sigmoid(self, x):
        self.x = x
        return 1 / (1 + math.e**(-x))

    def softmax(self, x):
        self.x = x
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def crossEntropy(self, yHat):
        self.yHat = yHat
        if self.y == 1:
            return -math.log(yHat)
        else:
            return -math.log(1-yHat)

    def feedForward(self):
        self.layer1 = self.sigmoid(np.dot(self.weight1, self.input) + self.b)
        self.layer2 = self.softmax(np.dot(self.weight2, self.layer1) + self.c)

    def backpropagation(self):
        #using Tensor / PyTorch (autograd) to do the differntiation
        weight2_d = weight2.grad()
        weight1_d = weight1.grad()

        self.weight1 += weight1_d
        self.weight2 += weight2_d