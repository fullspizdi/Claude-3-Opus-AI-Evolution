import torch
import torch.nn as nn
import torch.optim as optim
from utils import load_config

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_layers, output_size):
        super(NeuralNetwork, self).__init__()
        layers = [nn.Linear(input_size, hidden_layers[0]), nn.ReLU()]
        for i in range(1, len(hidden_layers)):
            layers.append(nn.Linear(hidden_layers[i-1], hidden_layers[i]))
            layers.append(nn.ReLU())
        layers.append(nn.Linear(hidden_layers[-1], output_size))
        layers.append(nn.LogSoftmax(dim=1))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        return self.model(x)

def get_model(config_path):
    config = load_config(config_path)
    model_params = config['model_params']
    model = NeuralNetwork(
        input_size=model_params['input_size'],
        hidden_layers=model_params['hidden_layers'],
        output_size=model_params['output_size']
    )
    return model

def get_optimizer(model, config_path):
    config = load_config(config_path)
    learning_rate = config['model_params']['learning_rate']
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    return optimizer

def save_model(model, path):
    torch.save(model.state_dict(), path)

def load_model(model, path):
    model.load_state_dict(torch.load(path))
    model.eval()
