#!/usr/bin/env python3
"""
Module to plot a histogram of student project grades.
"""
import matplotlib.pyplot as plt
import numpy as np


def frequency():
    """
    Plots a histogram of student grades with bins every 10 units,
    labeled axes, title, and black-outlined bars.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.show()


if __name__ == '__main__':
    frequency()
