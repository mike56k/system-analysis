import json
import numpy as np

def build_comparison_matrix(column):
    c = len(column)
    res = np.zeros((c, c))
    for index1 in range(c):
        for index2 in range(c):
            val = 0
            if column[index1] > column[index2]:
                val = 1
            elif column[index1] == column[index2]:
                val = 0.5
            res[index1][index2] = val
    return res

def task(input_matrix_json: str):
    input_matrix = np.array(json.loads(input_matrix_json)).T
    comparison_matrices = []
    for col in range(input_matrix.shape[1]):
        comparison_matrices.append(build_comparison_matrix(input_matrix[:,col]).T)
    mean_values = np.mean(comparison_matrices, axis=0)
    k0 = [1/input_matrix.shape[0] for i in range(input_matrix.shape[1])]
    y = np.dot(mean_values, k0)
    l = np.dot(np.ones(len(y)), y)
    k1 = np.dot(1/l, y)
    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(mean_values, k0)
        l = np.dot(np.ones(len(y)), y)
        k1 = np.dot(1/l, y)
    return json.dumps([round(el, 3) for el in k1])
