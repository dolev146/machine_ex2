import numpy as np

data = '''0.22 -0.98 -1
1.00 0.09 -1
-1.00 0.10 1
0.94 -0.34 -1
-0.90 0.43 1
0.89 -0.46 -1
-0.35 -0.94 -1
-0.56 0.83 1
0.23 0.97 1
0.83 -0.55 -1
0.58 0.81 1
-0.53 -0.85 -1
-0.62 0.79 1
-0.85 0.52 1
0.93 0.36 -1
-0.97 0.25 1
0.19 -0.98 -1
-0.91 0.41 1
-0.68 0.73 1
0.98 -0.18 -1
0.81 0.59 -1
-0.99 0.10 1
-0.42 0.91 1
0.54 -0.84 -1
-0.70 0.72 1
-1.00 0.01 1
0.03 -1.00 -1
0.31 -0.95 -1
1.00 0.04 -1
-0.99 0.16 1
0.99 -0.17 -1
-0.64 0.77 1
0.11 0.99 1
0.98 -0.17 -1
-0.15 -0.99 -1
-0.99 0.17 1
0.52 -0.85 -1
-0.40 0.91 1
0.98 -0.17 -1
0.90 0.44 -1
-0.95 0.31 1
-0.48 -0.88 -1
-0.91 0.41 1
-0.32 0.95 1
-0.99 -0.14 1
1.00 -0.05 -1
-1.00 0.08 1
-0.06 1.00 1
-0.16 0.99 1
0.12 0.99 1
0.97 0.24 -1
0.91 0.41 -1
-0.57 0.82 1
0.93 0.36 -1
0.90 -0.43 -1
0.75 0.66 -1
-0.99 -0.14 1
0.37 -0.93 -1
0.11 0.99 1
-0.90 0.43 1
0.98 -0.19 -1
-0.43 0.90 1
0.26 0.97 1
0.45 0.89 1
-0.72 -0.70 1
0.32 -0.95 -1
0.98 0.21 -1
-1.00 0.08 1
0.94 -0.34 -1
0.95 -0.31 -1
-0.93 0.38 1
0.84 -0.55 -1
0.84 0.55 -1
1.00 0.08 -1
-0.09 1.00 1
0.98 0.19 -1
-0.60 -0.80 -1
-0.62 -0.79 -1
-0.92 -0.40 1
0.96 0.27 -1
-0.96 0.28 1
1.00 -0.04 -1
-0.12 0.99 1
0.28 0.96 1
0.13 -0.99 -1
-0.76 -0.65 1
-0.60 -0.80 -1
-0.89 -0.46 1
0.86 -0.51 -1
-0.96 0.27 1
-0.03 -1.00 -1
-0.81 -0.58 1
0.31 -0.95 -1
-0.98 0.18 1
0.02 -1.00 -1
-0.99 -0.16 1
-0.30 0.95 1
0.99 -0.14 -1
0.09 -1.00 -1
0.97 0.23 -1
0.70 0.71 1
-0.69 0.72 1
-0.27 -0.96 -1
0.61 -0.79 -1
0.91 0.42 -1
-0.91 0.41 1
-0.61 0.80 1
-0.97 -0.23 1
-0.26 -0.97 -1
0.82 -0.57 -1
0.65 0.76 1
0.45 0.89 1
-0.90 0.44 1
0.51 -0.86 -1
0.24 0.97 1
0.21 0.98 1
-0.94 0.34 1
-0.75 -0.66 1
-0.87 -0.49 1
0.77 0.64 -1
0.30 -0.95 -1
-0.97 -0.25 1
-0.88 0.48 1
0.56 0.83 1
-0.50 -0.86 -1
0.31 0.95 1
-0.86 -0.51 1
-0.93 0.36 1
0.01 1.00 1
1.00 0.05 -1
-0.02 1.00 1
-0.92 0.39 1
-0.80 0.60 1
-0.44 -0.90 -1
0.96 0.26 -1
-0.95 0.32 1
-0.87 -0.50 1
-0.98 -0.21 1
-0.86 0.51 1
0.81 -0.59 -1
-0.47 0.88 1
0.73 0.68 -1
0.05 1.00 1
1.00 0.10 -1
0.26 0.96 1
-0.42 -0.91 -1
-0.44 0.90 1
-0.66 0.75 1
-0.76 -0.65 1
0.09 -1.00 -1
'''
parsed_data = [list(map(float, line.split())) for line in data.strip().split('\n')]
X = np.array([entry[:2] for entry in parsed_data])
y = np.array([entry[2] for entry in parsed_data])

def perceptron(X, y, n_iterations=1000):
    w = np.zeros(len(X[0]))
    mistakes = 0
    
    for _ in range(n_iterations):
        for i in range(len(X)):
            if y[i] * np.dot(X[i], w) <= 0:
                w += y[i] * X[i]
                mistakes += 1
                
    return w, mistakes

w, mistakes = perceptron(X, y)
print("Final direction vector:", w)
print("Number of mistakes made by the algorithm:", mistakes)


def margin(w, X, y):
    margins = [y[i] * np.dot(X[i], w) / np.linalg.norm(w) for i in range(len(X))]
    return min(margins)

margin_found = margin(w, X, y)
print("Margin achieved by the final direction vector:", margin_found)


import itertools

def brute_force_margin(X, y, step=0.01):
    best_margin = -np.inf
    best_w = None

    for w1, w2 in itertools.product(np.arange(-1, 1+step, step), repeat=2):
        if w1 == 0 and w2 == 0: # Skip the null vector
            continue
        w = np.array([w1, w2])
        current_margin = margin(w, X, y)
        if current_margin > best_margin:
            best_margin = current_margin
            best_w = w

    return best_margin, best_w

optimal_margin, optimal_w = brute_force_margin(X, y)
print("Optimal margin:", optimal_margin)
print("Difference between optimal margin and the margin found by Perceptron:", optimal_margin - margin_found)




