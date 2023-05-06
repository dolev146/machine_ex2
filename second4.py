import numpy as np
from itertools import product

def algorithm(data, labels, max_rounds=None):
    n = len(data)
    assert n == len(labels), "Data and labels must have the same length"

    w = np.zeros(data[0].shape)
    num_mistakes = 0

    round_count = 1
    while max_rounds is None or round_count <= max_rounds:
        mistake_found = False

        for i in range(n):
            xi = data[i]
            label = labels[i]

            if np.dot(w, xi) > 0:
                guess = 1
            else:
                guess = -1

            if guess != label:
                mistake_found = True
                num_mistakes += 1

                if label == 1:
                    w += xi
                else:
                    w -= xi

                break

        if not mistake_found:
            break

        round_count += 1

    return w, num_mistakes

def margin(w, data, labels):
    margins = [np.dot(w, xi) * label for xi, label in zip(data, labels)]
    return min(margins)

def optimal_margin_brute_force(data, labels):
    max_margin = 0
    for w1, w2 in product(np.linspace(-1, 1, 100), repeat=2):
        w = np.array([w1, w2])
        current_margin = margin(w, data, labels)
        max_margin = max(max_margin, current_margin)
    return max_margin

def read_data_from_file(file_path):
    data = []
    labels = []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            data_point = np.array([float(values[0]), float(values[1])])
            label = int(values[2])

            data.append(data_point)
            labels.append(label)

    return np.array(data), np.array(labels)

# Example usage
file_path = 'data.txt'
data, labels = read_data_from_file(file_path)

w, num_mistakes = algorithm(data, labels)
print("Resulting vector:", w)
print("Number of mistakes made by the algorithm:", num_mistakes)

final_margin = margin(w, data, labels)
print("Margin achieved by the final direction vector:", final_margin)

optimal_margin = optimal_margin_brute_force(data, labels)
print("Optimal margin (brute force):", optimal_margin)
print("Difference between optimal margin and the margin found by Perceptron:", optimal_margin - final_margin)
