from layer import *


class network:

    gennetwork=[]
    network_input = []
    next_layer_input =[]
    layer_number = 0

    def __init__(self, loss_function, learning_rate, wrh, wrl, wr_method, input):
        self.l_func = loss_function
        self.learn_rate = learning_rate
        self.wr = [wrl,wrh]
        self.wrm = wr_method
        self.network_input = input

    def add_hidden_layer(self, n_neurons, act_function, wtype, wrl, wrh, brl, brh):
        hid_layer = hiddenLayer(n_neurons, act_function, wtype, wrl, wrh, brl, brh)
        self.gennetwork.append(hid_layer)

    def add_input_layer(self, n_neurons, input):
        input_layer = inputLayer(n_neurons, input)
        self.gennetwork.append(input_layer)
    
    def add_output_layer(self, n_neurons, output_type):
        output_layer = outputLayer(n_neurons, output_type)
        self.gennetwork.append(output_layer)

    def forward_pass (self):
        net_size= len(self.gennetwork) - 1
        for i in range(1, net_size):
            next_input = self.gennetwork[i-1].get_layer_output()
            self.gennetwork[i].forward_pass(next_input)

        self.gennetwork[net_size].generate_ouput()

    def apply_error_function():
        pass

    def get_batches():
        pass

