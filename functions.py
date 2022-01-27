from xml.dom.pulldom import parseString
import numpy as np
import math as m


def sigmoid(x):
    result = 1/(1+m.exp(-x))
    return result


def tanh(x):
    result = (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))
    return result

def relu(x):
    return max(0,x)

def linear(x):
    return x

def MSE(x):
    pass

def cross_entropy(x):
    pass




