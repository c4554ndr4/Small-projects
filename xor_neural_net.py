# 2 -3- 1  (2 inputs, 3 hidden nodes, 1 output node)
# xor  classic example of training a neural network to learn the exclusive-or function
# note that xor is non-linear and thus cannot be done with only a single layer nor without any activation (sigmoid) layers

import math
import numpy as np

def sigmoid(x, derivative=False):
  return (np.multiply(x,(1-x))) if derivative else 1/(1+np.exp(-x))

#xor
training = [[0, 0], [1, 0], [0, 1], [1, 1]]
results = [0, 1, 1, 0]

weights1 = np.random.uniform(low=-1, high=1, size=(3, 2))
print("our starting random guess at our weights:",weights1)

weights2 = np.random.uniform(low=-1, high=1, size=(1, 3))
print("second layer of weights that we also have to learn know: ", weights2.shape, " values:  ",weights2)

out1 = 0
out2 = 0


alpha = 0.025  # learning rate small enough to not diverge

def forward(x):
    global out1, out2
    out1 = np.matmul(weights1, x) #after first set of weights applied
    out2 = sigmoid(out1)
    return np.matmul(weights2, out2)

def train_sample(x, p):
    global weights1, weights2
    global alpha
    y = forward(x)
    e = y - p
    e2 = np.matmul(e, weights2) #derivative of weights2 times x is just weights2
    e1 = np.multiply(e2,sigmoid(out2, True)) #derivative of sigmoid uses the y as the input
    weights2 = weights2 - np.outer(e, out2) * alpha # out2 is global from the feed forward
    weights1 = weights1 - np.outer(e1 , x) * alpha
    return np.dot(e,e) #return the error for this sample


def train_batch():
    batchsize = 5000
    for k in range(10):
        sse=0
        for j in range(batchsize):
            for i in range(len(training)):
                x = training[i]
                p = [results[i]]
                sse += train_sample(x,p)
        print("rmse: ", math.sqrt(sse/batchsize))
        #print("new weights1-actual is: ", weights1-actual)
        #print("new weights2-actual2 is: ", weights2-actual2)


train_batch()
print("new weights1 is: ", weights1)
print("new weights2 is: ", weights2)

for x in training:
    print(x)
    print('feed-forward for input: ', x,' result: ', forward(x))
