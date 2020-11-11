import TicTacToe
from NeuralNet import NeuralNet
import numpy as np

if __name__ == "__main__":
    training_data = TicTacToe.create_sample(100)

    layers_definition = {
        "input": 9,
        "hidden": 9,
        "n_hidden": 4,
        "output": 3,
    }

    nn = NeuralNet(layers_definition)
