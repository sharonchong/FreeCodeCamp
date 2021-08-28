import numpy as np


def calculate(list):
    try:
        ls = np.reshape(list, (3, 3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    mean = [
        np.mean(ls, axis=0).tolist(),
        np.mean(ls, axis=1).tolist(),
        np.mean(ls)
    ]
    var = [
        np.var(ls, axis=0).tolist(),
        np.var(ls, axis=1).tolist(),
        np.var(ls)
    ]

    std = [
        np.std(ls, axis=0).tolist(),
        np.std(ls, axis=1).tolist(),
        np.std(ls)
    ]

    max = [
        np.max(ls, axis=0).tolist(),
        np.max(ls, axis=1).tolist(),
        np.max(ls)
    ]
    min = [
        np.min(ls, axis=0).tolist(),
        np.min(ls, axis=1).tolist(),
        np.min(ls)
    ]
    sum = [
        np.sum(ls, axis=0).tolist(),
        np.sum(ls, axis=1).tolist(),
        np.sum(ls)
    ]

    #create dictionary with calcs
    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max,
        'min': min,
        'sum': sum
    }

    return calculations
