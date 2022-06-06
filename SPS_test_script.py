"""
Created on Mon Jun  6 23:25:47 2022

@author: yipjiaqi
https://github.com/Yip-Jia-Qi/poisson-gap-sampling
"""

import matplotlib.pyplot as plt
from SPS import SPS

def plotSPS(v):
    gaps = []
    for i in range(len(v)-1):
        gaps.append(v[i+1]-v[i])
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(v)
    ax2.plot(gaps)
    return

if __name__ == '__main__':
    import numpy as np
    rng = np.random.default_rng(42)
    for i in range(5):
        test = SPS(102, 1024, rng)
        plotSPS(test)
