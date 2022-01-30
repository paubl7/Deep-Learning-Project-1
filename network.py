
from tkinter import N
from layer import *


class network:

    gennetwork=[]

    def __init__(self, loss_function, learning_rate, weight_reg, wr_method):
        self.l_func = loss_function
        self.learn_rate = learning_rate
        self.wr = weight_reg
        self.wrm = wr_method

    def add_hidden_layer(self, n_neurons, act_function, wtype, wrl, wrh, brl, brh):
        hid_layer = hiddenLayer(n_neurons, act_function, wtype, wrl, wrh, brl, brh)
        self.gennetwork.append(hid_layer)

    def add_input_layer(self, n_neurons, wtype, wrl, wrh, brl, brh):
        input_layer = inputLayer(n_neurons, wtype, wrl, wrh, brl, brh)
        self.gennetwork.append(input_layer)
    
    def add_output_layer(self, n_neurons, output_type):
        output_layer = outputLayer(n_neurons, output_type)
        self.gennetwork.append(output_layer)
