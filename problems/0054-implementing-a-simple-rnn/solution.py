import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    hh = initial_hidden_state
    for item in input_sequence:
        h_t = np.tanh(np.dot(Wx, item) + np.dot(Wh, hh) + b)
        hh = h_t
    return nh_t