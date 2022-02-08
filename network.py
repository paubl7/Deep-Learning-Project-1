from layer import *


class network:

    gennetwork=[]
    network_input = []
    next_layer_input =[]
    layer_number = 0

    def __init__(self, loss_function, learning_rate, wrh, wrl, wr_method):
        self.l_func = loss_function
        self.learn_rate = learning_rate
        self.wr = [wrl,wrh]
        self.wrm = wr_method

    def add_hidden_layer(self, n_neurons, act_function, wtype, wrl, wrh, brl, brh):
        prev_neurons = self.gennetwork[len(self.gennetwork)-1].n_neurons
        hid_layer = hiddenLayer(n_neurons, prev_neurons, act_function, wtype, wrl, wrh, brl, brh)
        self.gennetwork.append(hid_layer)

    def add_input_layer(self, n_neurons):
        input_layer = inputLayer(n_neurons)
        self.gennetwork.append(input_layer)
    
    def add_output_layer(self, n_neurons, output_type):
        output_layer = outputLayer(n_neurons, output_type)
        self.gennetwork.append(output_layer)

    def forward_pass (self, input):
        self.gennetwork[0].generate_output(input)
        next_input = self.gennetwork[0].get_layer_output()
        print("output input layer:")
        print(next_input)
        for i in range(1, len(self.gennetwork)-2):
            self.gennetwork[i].forward_pass(next_input)
            next_input = self.gennetwork[i].get_layer_output()
            print("output layer", i)
            print(next_input)
        
        self.gennetwork[len(self.gennetwork)-1].generate_output(next_input)
        print(self.gennetwork[len(self.gennetwork)-1].get_layer_output())



    def apply_error_function():
        pass

    def get_batches():
        pass
    
    def fit():
        pass

    def backward_pass():
        pass

    
    def prediction(self, result):
        #REMEMBER DOT FUNCTION BETWEEN TWO VECTORS
        pass
