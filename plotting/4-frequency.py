#!/usr/bin/env python3
"""Module that plots a histogram of student scores."""
import numpy as np
import matplotlib.pyplot as plt


def frequency(student_grades):
    """Plots a histogram of student scores for a project."""
    plt.figure(figsize=(6.4, 4.8))
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.show()

if __name__ == '__main__':
    frequency()
