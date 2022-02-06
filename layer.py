
import numpy as np
import functions as fnc
from numpy import random

class layer:
    layeroutput=[]
    

    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
    
    def get_layer_ouput(self):
        return self.layeroutput

    
class hiddenLayer(layer):

    weight_array=[]
    bias_array = []

    def __init__(self, n_neurons, act_function, wtype, wrl, wrh, brl, brh):
        super().__init__(n_neurons)
        self.act_function = act_function
        self.wtype = wtype
        if (self.wtype == "range"):
            self.weight_array= random.uniform(wrl,wrh, n_neurons)
        #elif(self.wtype == "glorot"):
            pass ##ESTABLIR COM FA LA DISTRIBUCIO DE GLOROT
        self.array = random.uniform(brl,brh,n_neurons)

        
    def forward_pass(self, layer_input):
        resized_input = np.resize(layer_input,self.n_neurons)

        weighted_input = [resized_input[i]*self.weight_array[i] for i in range(0,self.n_neurons-1)]
        biased_input = [weighted_input[i] + self.bias_array[i] for i in range(0,self.n_neurons-1)]
            
        if (self.act_function == "sigmoid"):
            self.layeroutput= [fnc.sigmoid(bi) for bi in biased_input]
        elif (self.act_function == "tanh"):
            self.layeroutput= [fnc.tanh(bi) for bi in biased_input]
        elif (self.act_function == "linear"):
            self.layeroutput= [fnc.linear(bi) for bi in biased_input]
        elif (self.act_function == "relu"):
            self.layeroutput= [fnc.relu(bi) for bi in biased_input]

            
            
class inputLayer(layer):

    def __init__(self, n_neurons, input):
        super.__init__(n_neurons)
        self.layeroutput = np.resize(input, self.n_neurons)
        

class outputLayer(layer):
    def __init__(self, n_neurons, output_type):
        super.__init__(n_neurons)
        self.type = output_type

    def generate_output(self, input):
        if (self.type == "softmax"):
            self.layeroutput = [fnc.softmax(out) for out in input]
        
        else: 
            self.layeroutput = input