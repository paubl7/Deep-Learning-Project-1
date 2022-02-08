from operator import ge
import numpy as np
import string
from functions import softmax
import network as nt
import datagenerator as dg
import argparse
import os
import sys


generated_network = nt.network("MSE",0.1,0.1,1,"a",)

def add_input_layer(n_neurons):
        generated_network.add_input_layer(n_neurons)

def add_hidden_layer(n_neurons, act_function, wtype, wrl, wrh, brl, brh):
    generated_network.add_hidden_layer(n_neurons, act_function, wtype, wrl,wrh,brl,brh)

def add_output_layer(n_neurons, output_type):
    generated_network.add_output_layer(n_neurons,output_type)

def document_parser ():
    pass

def create_config_file(config_path):
    i=0
    created = False
    filepath = ""
    while(not created):
        filename = "config"+str(i)+".txt"
        filepath = os.path.join(config_path, filename)
        if (not os.path.exists(filepath)):
            return filepath
        i+=1
    
    
    


if __name__ == '__main__':
   add_input_layer(24)
   add_hidden_layer(15, "relu", "range", 0.1, 1, 0, 1)
   add_hidden_layer(20, "linear", "range", 0.1, 1, 0, 1)
   add_hidden_layer(25, "sigmoid", "range", 0.1, 1, 0, 1)
   add_output_layer(20, "softmax")

   input = np.array([0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,1])
   generated_network.forward_pass(input)