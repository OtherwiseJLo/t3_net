import numpy as np
from typing import Dict
from TicTacToe import Board


def sigmoid(x):
    return 2 / (1 + np.exp(-x)) - 1


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


class InputLayer:
    def __init__(self, input_size, hidden_size):
        self.nodes = np.zeros(input_size)
        self.weights = np.random.uniform(-1, 1, [input_size, hidden_size])

    def load(self, data):
        self.nodes = data

    def feed_forward(self, hidden_layer):
        hidden_layer.nodes[0] = sigmoid(np.dot(self.nodes, self.weights))


class HiddenLayer:
    def __init__(self, hidden_size, n_hidden_layers):
        self.nodes = np.zeros([n_hidden_layers, hidden_size])
        self.weights = np.random.uniform(
            -1, 1, [n_hidden_layers-1, hidden_size, hidden_size]
        )

    def feed_forward(self):
        for i in range(self.weights.shape[0]):
            self.nodes[i+1] = sigmoid(np.dot(self.nodes[i], self.weights[i]))


class OutputLayer:
    def __init__(self, output_size, hidden_size):
        self.nodes = np.zeros(output_size)
        self.weights = np.random.uniform(-1, 1, [hidden_size, output_size])

    def feed_forward(self, hidden_layer):
        self.nodes = sigmoid(np.dot(hidden_layer.nodes[-1], self.weights))

    def score(self):
        return np.argmax(np.abs(self.nodes))-1


class NeuralNet:
    def __init__(self, layers: Dict):
        self.input_layer = InputLayer(layers["input"], layers["hidden"])
        self.hidden_layer = HiddenLayer(layers["hidden"], layers["n_hidden"])
        self.output_layer = OutputLayer(layers["output"], layers["hidden"])
        self.error = None

    def feed_forward(self, sample_board: Board):
        self.input_layer.load(sample_board.array)
        self.input_layer.feed_forward(self.hidden_layer)
        self.hidden_layer.feed_forward()
        self.output_layer.feed_forward(self.hidden_layer)
        self.error = np.sum((sample_board.truth - self.output_layer.nodes)**2)

    def backpropogate(self):
        pass
