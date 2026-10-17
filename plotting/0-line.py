#!/usr/bin/env python3
"""
Module to plot y as a line graph using matplotlib and numpy.
"""
import matplotlib.pyplot as plt
import numpy as np


def line():
    """
    Plots y = np.arange(0, 11) ** 3 as a solid red line
    with the x-axis ranging from 0 to 10.
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, 'r-')
    plt.xlim(0, 10)
    plt.show()


if __name__ == '__main__':
    line()
