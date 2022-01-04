from random import randint as rand
from os.path import exists
from math import exp
from matplotlib import pyplot as plt

class Perceptron_OR_Gate:

    def __init__(self):
        self.Eta = 0.1

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

        # decision boundary intercepts for all 
        # remembered dbs
        self.db_x_coords = []
        self.db_y_coords = []
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
        savefile = "Perceptron_Weights_OR_"+str(self.weight_file_num) +".txt"
        while exists(savefile):
            self.weight_file_num += 1
            savefile = "Perceptron_Weights_OR_"+str(self.weight_file_num)+".txt"
        
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
        if self.Weight_File == None:
            self.init_weights()
            self.save_weights()
        else:
            self.load_weights()

        i = -1
        for example in self.Training_Data:
            if len(self.accuracies) > 1:
                x = self.accuracies[-1] - self.accuracies[-2]
                if x < 0:
                    x = x * -1
                if x < 0.0001:
                    print("\n\nEpoch "+str(i)+") Acc: "+str(self.accuracies[-1])+"%")
                    return

        # example: [input, input, target_output]

            self.forward_propagate(example)
            self.compute_accuracy(self.output, example[2])
            self.update_decision_boundary()

            i += 1
            if i % 25 == 0:
                print("\n\nEpoch "+str(i)+") Acc: "+str(self.accuracies[-1])+"%")
        

            if self.output != example[2]:
                self.back_propagate(self.output, example[2])

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
        
        
    
    def back_propagate(self, output, target):
        # update weights
        # weight_i+1 = weight_i + eta * (output - target) * input_i
        d1 = self.Eta
        d2 = output - target
        for i in range(len(self.inputs)):
            d3 = self.inputs[i]
            delta = d1 * d2 * d3
            self.weights[i] -= delta
    
    def sigma(self, z):
        # outputs 0 < x < 1
        s1 = 0 - z
        if s1 > 700:
            s1 = 700
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
    
    def update_decision_boundary(self):
        x_coords = [-self.weights[0] / self.weights[2], 0]
        y_coords = [0, -self.weights[0]/self.weights[1]]

        self.db_x_coords.append(x_coords.copy())
        self.db_y_coords.append(y_coords.copy())

    def graph_decision_boundary(self):
        plt.ylim(0,1)
        plt.xlim(0,1)

        # or data polts
        or_y = [0,0,1,1]
        or_x = [0,1,0,1]


        fig, ax = plt.subplots()
        ax.plot(or_x, or_y, 'o')


        print("Dbs: "+str(len(self.db_y_coords)))
        for i in range(50):
            if i % 10 == 0 or i == 49:
                ax.plot(self.db_x_coords[i], self.db_y_coords[i], label="DB"+str(i))
        
        plt.legend()
        plt.show()



        



#testing
perceptron = Perceptron_OR_Gate()
perceptron.load_data("TRAINING", "training_data_OR_1000.txt")
perceptron.Weight_File = "Perceptron_Weights_OR_0.txt"
perceptron.Train_Perceptron()
perceptron.save_weights()
perceptron.graph_decision_boundary()
#perceptron.graph_training_accuracy()
