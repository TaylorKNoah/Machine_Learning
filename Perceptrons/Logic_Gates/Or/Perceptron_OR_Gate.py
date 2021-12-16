from random import randint as rand
class Perceptron_OR_Gate:

    def __init__(self):
        self.Gamma = 0.1

        self.inputs = [1,0,0]
        self.weights = [[0, 0, 0], [0, 0, 0]]
        self.output = 0

        self.Training_Data = []
        self.Testing_Data = []

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



