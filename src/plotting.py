# -*- coding: utf-8 -*-
"""
Created on Thu Sep 2 15:03:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    def __init__(self, result_data, file_name):
        self.result = result_data
        self.filename = file_name

    def extract_xy(self):
        # Getting the xy data
        xy_data = self.result.xy_data
        x = xy_data[:, 0]
        y = xy_data[:, 1]

        return x, y

    def plot_xy_data(self, x_title=None, y_title=None):
        """ This function generates a plot data points, stiffness slope, offset line """

        # Preparing for single plot
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Getting the xy data
        x, y = self.extract_xy()

        plt.ylim(0, max(y)+0.1*max(y))
        plt.xlim(0, max(x))

        # Plotting xy data
        ax.plot(x, y, 'r')

        # Calculate the stiffness line
        XY = self.result.stiffness_line()
        max_index = np.argmax(y)

        # Plotting stiffness line
        ax.plot(XY[0:max_index, 0], XY[0:max_index, 1], 'k', linewidth=1)

        # Calculate the offset line
        XY_offset = self.result.offset_line()

        # Plotting the offset line
        ax.plot(XY_offset[0:max_index, 0], XY_offset[0:max_index, 1], 'g', linewidth=1)

        # Getting the points of the stiffness line
        point1 = self.result.point1
        point2 = self.result.point2

        # Plotting points
        ax.plot(point1.x, point1.y, 'ro', markersize='5',
                markerfacecolor='red', markeredgewidth='1',
                markeredgecolor='k')
        ax.plot(point2.x, point2.y, 'ro', markersize='5',
                markerfacecolor='red', markeredgewidth='1',
                markeredgecolor='k')

        # Assigning the x_title
        if x_title is None:
            ax.set_xlabel(self.result.x_title)
        else:
            ax.set_xlabel(x_title)

        # Assigning the y_title
        if y_title is None:
            ax.set_ylabel(self.result.y_title)
        else:
            ax.set_ylabel(y_title)

        fig.savefig(self.filename + "_xy" + ".png")

        return ax
