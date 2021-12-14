from random import randint as rand
import json


class Data_Generator:
    
    def __init__(self):
        return

    def generate_OR_data(self, filename, num_data):

        if num_data % 4 != 0:
            print("Usage: Data_Generator.generate_OR_data(filename.txt numdata). Where num_data % 4 == 0.")
            return

        # or gate
        # choice = [input, input, output]
        possible_choices = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

        # num allowed per choice
        a = num_data / 4
        allowance = [a, a, a, a]

        data = []

        i = 0
        while(i < num_data):
            r = rand(0, 3)
            if allowance[r] > 0:
                allowance[r] -= 1
                data.append(possible_choices[r].copy())
                i += 1


        with open(filename, "w") as file:
            for example in data:
                file.write('%s\n' % example)
