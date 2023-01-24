#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def main():
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    plt.plot(xpoints, ypoints)
    plt.show()


if __name__ == '__main__':
    main()