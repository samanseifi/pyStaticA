# -*- coding: utf-8 -*-
"""
Created on Thu Sep 2 15:03:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_xy_data(result):
    """ This function generates a plot data points, stiffness slope, offset line """

    # Preparing for single plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Getting the xy data
    xy_data = result.xy_data
    x = xy_data[:, 0]
    y = xy_data[:, 1]

    # Plotting xy data
    ax.plot(x, y, 'r')

    # Calculate the stiffness line
    XY = result.stiffness_line()
    max_index = np.argmax(y)

    # Plotting stiffness line
    ax.plot(XY[0:max_index, 0], XY[0:max_index, 1], 'k', linewidth=1)

    # Calculate the offset line
    XY_offset = result.offset_line()

    # Plotting the offset line
    ax.plot(XY_offset[0:max_index, 0], XY_offset[0:max_index, 1], 'g', linewidth=1)

    # Getting the points of the stiffness line
    point1 = result.point1
    point2 = result.point2

    # Plotting points
    ax.plot(point1.x, point1.y, 'ro', markersize='5',
            markerfacecolor='red', markeredgewidth='1',
            markeredgecolor='k')
    ax.plot(point2.x, point2.y, 'ro', markersize='5',
            markerfacecolor='red', markeredgewidth='1',
            markeredgecolor='k')

    ax.set_xlabel(result.x_title)
    ax.set_ylabel(result.y_title)
    fig.savefig("plot1.png")

    return ax
