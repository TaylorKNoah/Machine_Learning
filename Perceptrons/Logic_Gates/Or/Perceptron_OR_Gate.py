from random import randint as rand
from os import exists

class Perceptron_OR_Gate:

    def __init__(self):
        self.Gamma = 0.1

        self.inputs = [1,0,0]
        self.weights = [0,0,0]
        self.output = 0

        self.Training_Data = []
        self.Testing_Data = []

        self.weight_file_num = 0
        return

    def load_data(self, TYPE, FILE):
        if TYPE != "TESTING" and TYPE != "TRAINING":
            print("Perceptron_OR_Gate.load_data usage(TYPE, FILE)")
            print("Where:")
            print("-TYPE must wither be \"TESTING\" or \"TRAINING\"")
            print("-FILE must be a file location")
            return

        data = []
        with open(FILE, "r") as file:
            for line in file:
                line_data = line[:-1]
                data.append(line_data)

        if TYPE == "TRIANING":
            self.Training_Data = data.copy()
        elif TYPE == "TESTING":
            self.Testing_Data = data.copy()
    
    def init_weights(self):
        for i in range(2):
            for j in range(3):
                r = rand(-50, 50) / 100
                self.weights[i][j] = r
    
    def save_weights(self):
        # find unused file name
        savefile = "Perceptron_Weights_OR_"+str(self.weight_file_num)
        while exists(savefile):
            self.weight_file_num += 1
        
        # save weights to unused file
        with open (savefile, "w") as File:
            for w in self.weights:
                File.write('%s\n' % w)
    
    def Train_Perceptron(self):
        # method
        # 0) init weights randomly
        # 1) get inputs
        # 2) forward propagate
        # 3) if incorrect output: Backpropagate
        # 4) Backpropagate
        # 5) Finish when all training examples sent through perceptron

        # 0)
        self.init_weights()

        # example: [input, input, target_output]
        for example in self.Training_Data:
            # 1)
            self.forward_propagate(example)


    def forward_propagate(self, example):
        # load inputs
        self.inputs[1] = example[0]
        self.inputs[2] = example[1]

        # compute XW
        self.output = 0
        for i in range(3):
            self.output += (self.inputs[i] * self.weights[i])
        

