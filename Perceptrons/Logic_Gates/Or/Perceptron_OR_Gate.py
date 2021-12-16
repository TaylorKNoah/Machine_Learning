
def Perceptron_OR_Gate:

    def __init__(self):
        self.Gamma = 0.1
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



