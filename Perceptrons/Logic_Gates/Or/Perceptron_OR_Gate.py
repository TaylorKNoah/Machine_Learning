

def Perceptron_OR:

    def __init__(self):
        return

    def read_data(self, filename):
        data = []

        with open(filename, "r") as file:
            for line in file:
                line_data = line[:-1]
                data.append(line_data)



