from typing import NamedTuple, Tuple
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Arc
import common


X =  np.array([[0.85794562, 0.84725174],
               [0.6235637,  0.38438171],
               [0.29753461, 0.05671298],
               [0.27265629, 0.47766512],
               [0.81216873, 0.47997717],
               [0.3927848,  0.83607876],
               [0.33739616, 0.64817187],
               [0.36824154, 0.95715516],
               [0.14035078, 0.87008726],
               [0.47360805, 0.80091075],
               [0.52047748, 0.67887953],
               [0.72063265, 0.58201979],
               [0.53737323, 0.75861562],
               [0.10590761, 0.47360042],
               [0.18633234, 0.73691818]])
K = 6
Mu = np.array([[0.6235637,  0.38438171],
               [0.3927848,  0.83607876],
               [0.81216873, 0.47997717],
               [0.14035078, 0.87008726],
               [0.36824154, 0.95715516],
               [0.10590761, 0.47360042]])
Var = np.array([0.10038354, 0.07227467, 0.13240693, 0.12411825, 0.10497521, 0.12220856])
P = np.array([0.1680912,  0.15835331, 0.21384187, 0.14223565, 0.14295074, 0.17452722])
ll = -1655.170056
print(X.shape, Mu.shape, Var.shape, P.shape)
print(common.bic(X, mixture= (Mu, Var, P), log_likelihood = ll))


### Result should be -1686.312633

x = (- 1686.312633 + 1655.170056) * -2
print(x / np.log(15))

y = (- 1453.539804 + 1398.871858) * -2
print(y / np.log(12))