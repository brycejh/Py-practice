import numpy as np
import pandas
import matplotlib.pyplot as plt


#
zerO = np.zeros(10)
onE = np.ones(11)
emptY = np.empty(12)
print(zerO)
print(onE)
print(emptY)

d2 = np.array(
    [
        np.arange(5),
        np.flip(np.arange(5)),
        np.arange(5),
        np.flip(np.arange(5)),
        np.arange(5),
    ]
)
print(d2)
print(np.unique(d2))
print(sum(np.arange(5)))
print(sum(d2))
print(d2.sum(axis=1))
#
