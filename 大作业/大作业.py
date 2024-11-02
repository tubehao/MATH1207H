import numpy as np
import matplotlib.pyplot as plt

# miu1 = np.random.uniform(-10, 10)
# miu2 = np.random.uniform(-10, 10)
# cegema1 = np.random.uniform(0, 2)
# cegema2 = np.random.uniform(0, 2)

miu1 = 1
miu2 = 2
cegema1 = 1
cegema2 = 1.5


# yitap = np.random.uniform(0, 1)
yitap = 0.8
yita = [0, 1]
yitaProb = [1-yitap, yitap]
p = np.random.choice(yita, p=yitaProb)

def mixedGauss(x, miu1, miu2, cegema1, cegema2, yita):
    zlist = []
    for _ in range(5):
        X = np.random.normal(miu1, cegema1)
        Y = np.random.normal(miu2, cegema2)
        Z = np.exp(-(x - miu1) ** 2 / (2 *(cegema1)**2)) / (np.sqrt(2 * np.pi * cegema1)) + p * np.exp(
        -(x - miu2) ** 2 / (2 * cegema2)) / (np.sqrt(2 * np.pi * cegema2))
        zlist.append(Z)
    return zlist

print(mixedGauss(1, miu1, miu2, cegema1, cegema2, yitap))
