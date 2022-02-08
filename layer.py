
import numpy as np
import functions as fnc
from numpy import random

class layer:
    layeroutput=[]
    

    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
    
    def get_layer_output(self):
        return self.layeroutput
    
    def generate_wt(self, x, y, wrl, wrh):
        l=  np.random.uniform(wrl,wrh, (y,x))
        return l

    
class hiddenLayer(layer):

    weight_array=[]
    bias_array = []

    def __init__(self, n_neurons,prev_neurons, act_function, wtype, wrl, wrh, brl, brh):
        super().__init__(n_neurons)
        self.act_function = act_function
        self.connected_layer_neurons= prev_neurons
        self.wtype = wtype
        #if (self.wtype == "range"):
        self.weight_array= self.generate_wt(n_neurons, prev_neurons, wrl, wrh)
        #elif(self.wtype == "glorot"):
            #pass ##ESTABLIR COM FA LA DISTRIBUCIO DE GLOROT
        self.bias_array = np.ones(self.n_neurons)
        
    def forward_pass(self, layer_input):

        biased_input = layer_input.dot(self.weight_array) + self.bias_array
            
        if (self.act_function == "sigmoid"):
            self.layeroutput= fnc.sigmoid(biased_input) 
        elif (self.act_function == "tanh"):
            self.layeroutput= fnc.tanh(biased_input) 
        elif (self.act_function == "linear"):
            self.layeroutput= fnc.linear(biased_input)
        elif (self.act_function == "relu"):
            self.layeroutput= fnc.relu(biased_input)

            
class inputLayer(layer):

    def __init__(self, n_neurons):
        super().__init__(n_neurons)
        
    def generate_output(self,input):
        self.layeroutput =  input.reshape(1, len(input)) 
        

class outputLayer(layer):
    def __init__(self, n_neurons, output_type):
        super().__init__(n_neurons)
        self.type = output_type

    def generate_output(self, input):
        print("ouput of the forward")
        if (self.type == "softmax"):
            self.layeroutput = [fnc.softmax(out) for out in input]
        
        else: 
            self.layeroutput = input