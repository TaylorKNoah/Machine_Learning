from random import randint as rand
from os.path import exists
from math import exp
from matplotlib import pyplot as plt

class Perceptron_OR_Gate:

    def __init__(self):
        self.Gamma = 0.1

        self.inputs = [1,0,0]
        self.weights = [0,0,0]
        self.output = 0

        self.Weight_File = None
        self.weight_file_num = 0

        self.Training_Data = []
        self.Testing_Data = []

        self.training_correct = 0
        self.training_total = 0
        self.accuracies = []
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
                data.clear()
                line_data = line[:-1]

                data.append(int(line_data[1]))
                data.append(int(line_data[4]))
                data.append(int(line_data[7]))

                if TYPE == "TRAINING":
                    self.Training_Data.append(data.copy())
                elif TYPE == "TESTING":
                    self.Testing_Data.append(data.copy())
    
    def init_weights(self):
            for i in range(3):
                r = rand(-50, 50) / 100
                self.weights[i] = r
    
    def save_weights(self):
        # find unused file name
        savefile = "Perceptron_Weights_OR_"+str(self.weight_file_num)
        while exists(savefile):
            self.weight_file_num += 1
            savefile = "Perceptron_Weights_OR_"+str(self.weight_file_num)
        
        # save weights to unused file
        with open (savefile, "w") as File:
            for w in self.weights:
                File.write('%s\n' % w)
    
    def load_weights(self):
        i = 0
        with open(self.Weight_File, "r") as file:
            for line in file:
                self.weights[i] = float(line)
                i += 1

    def Train_Perceptron(self):
        # method
        # 0) init weights randomly
        # 1) get inputs
        # 2) forward propagate
        # 3) if incorrect output: Backpropagate
        # 4) Backpropagate
        # 5) Finish when all training examples sent through perceptron

        # 0)
        if self.Weight_File == None:
            self.init_weights()
        else:
            self.load_weights()

        # example: [input, input, target_output]
        i = -1
        #for example in self.Training_Data:
        for k in range(10):
            i += 1
            # 1)
            #self.forward_propagate(example)
            self.forward_propagate(self.Training_Data[i])

            print("\n\nExample "+str(i)+"): "
            +"\nInput: "+str(self.Training_Data[i][0])+", "+str(self.Training_Data[i][1])
            +"\nTarget: "+str(self.Training_Data[i][2])
            +"\nOutput: "+str(self.output))
        
            self.compute_accuracy(self.output, self.Training_Data[i][2])

    def forward_propagate(self, example):
        # load inputs
        self.inputs[1] = example[0]
        self.inputs[2] = example[1]

        # compute XW + W_0
        sum = 0
        for i in range(3):
            sum += (self.inputs[i] * self.weights[i])
        
        # compute activation
        activation = self.sigma(sum)

        # determine output
        if activation < 0.5:
            self.output = 0
        else:
            self.output = 1
    
    def sigma(self, z):
        # outputs 0 < x < 1
        s1 = 0 - z
        s2 = exp(s1)
        s3 = 1 + s2
        s4 = 1 / s3
        return s4
    
    def compute_accuracy(self, output, target):
        if output == target:
            self.training_correct += 1
        self.training_total += 1

        acc = self.training_correct / self.training_total

        self.accuracies.append(acc)

        return acc
    
    def graph_training_accuracy(self):
        plt.plot(self.accuracies)
        plt.ylabel("Accuracy")
        plt.xlabel("Epoch")
        plt.show()

        



#testing
perceptron = Perceptron_OR_Gate()
perceptron.load_data("TRAINING", "training_data_OR_100.txt")
perceptron.Weight_File = "Perceptron_Weights_OR_0"
perceptron.Train_Perceptron()
perceptron.graph_training_accuracy()