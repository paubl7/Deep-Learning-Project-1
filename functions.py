from xml.dom.pulldom import parseString
import numpy as np
import math as m

def sigmoid(x):
    return 1/(1+m.exp(-x))

def tanh(x):
    return (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))

def relu(x):
    return x * (x > 0)

def linear(x):
    return x

def MSE(predicted_vals, true_vals):
    difference_array = np.subtract(predicted_vals, true_vals)
    squared_array = np.square(difference_array)
    return squared_array.mean()
 
def cross_entropy(true_values,predicted_values):
  loss=-np.sum(true_values*np.log(predicted_values))
  return loss/float(predicted_values.shape[0])


def softmax(x):
  return np.exp(x)/np.sum(np.exp(x),axis=0)





