# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""
import pandas as pd
import numpy as np

import csv
import os


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class AnalysisOutput:
    def __init__(self, xy_data, x_title, y_title, stiffness,
                 point1, point2, yield_point, ultimate_point, offset):
        self.xy_data = xy_data
        self.x_title = x_title
        self.y_title = y_title
        self.stiffness = stiffness
        self.point1 = point1
        self.point2 = point2
        self.yield_point = yield_point
        self.ultimate_point = ultimate_point
        self.offset = offset

    def stiffness_line(self):
        """ Calculate stiffness line for visualizations """
        x1 = self.point1.x
        y1 = self.point1.y

        x2 = self.point2.x
        y2 = self.point2.y

        # Find the stiffness equation of line between point1 and point2
        x = self.xy_data[:, 0]

        # Equation of the line:
        y = y2 + (y2 - y1) / (x2 - x1) * (x - x2)

        XY = np.zeros([len(x), 2])
        XY[:, 0] = x
        XY[:, 1] = y

        return XY

    def offset_line(self):
        XY_offset = self.stiffness_line()

        x = self.xy_data[:, 0]

        XY_offset[:, 0] = XY_offset[:, 0] + self.offset * self.point1.x

        return XY_offset


def extract_xy_data(filename):
    # Finding the file format: csv is recommended.``
    file_name, file_extension = os.path.splitext(filename)

    # Check if the file format is in csv if not translate
    # TODO: Capabilities to translate or read other formats
    if file_extension == '.csv':

        # Reading xy data file
        xy_data = pd.read_csv(filename)

    elif file_extension == '.txt':
        print('File format is in txt. Translating to csv...')

        in_txt = csv.reader(open(filename, "rb"), delimiter='\t')
        filename_csv = filename + '.csv'
        out_csv = csv.writer(open(filename_csv, 'wb'))

        out_csv.writerows(in_txt)

        # Reading xy data file
        xy_data = pd.read_csv(filename_csv)
    else:  # Not supported formats
        print('ERROR: File format is not valid! Save your data in csv format.')

    # Reading data file header list
    headers_list = list(xy_data.columns.values)

    if len(headers_list) > 2:
        print("ERROR: x-y data file contains more than two columns!")

    # The x-axis label and y-axis label are taken from the first rows of the xy data
    x_title = headers_list[0]
    y_title = headers_list[1]

    # Change to numpy arrays
    xy_data = np.array(xy_data)

    return x_title, y_title, xy_data


def calculate_stiffness(xy_data, x1, x2):
    """ This function calculates the stiffness from the input file x1 and x2x2
    also it returns two Point class """

    # Find the y-value (y1) of x1 and then create a point
    y1_index = np.argwhere(np.diff(np.sign(xy_data[:, 0] - x1))).flatten()
    y1 = xy_data[y1_index[0]][1]
    point1 = Point(x1, y1)

    # Find the y-value (y2) of x2 and then create a point
    y2_index = np.argwhere(np.diff(np.sign(xy_data[:, 0] - x2))).flatten()
    y2 = xy_data[y2_index[0]][1]
    point2 = Point(x2, y2)

    # Now calculate the stiffness (slope of the linear portion)
    stiffness = (y2 - y1) / (x2 - x1)

    # Returning two Point class and a float (stiffness)
    return point1, point2, stiffness


def calculate_yield_point(xy_data, offset, point1, point2):
    """ This function find and calculate the offset yield point and returns
    the offset line y_offset = ax + b """

    # Get points coordinates
    x1 = point1.x
    y1 = point1.y

    x2 = point2.x
    y2 = point2.y

    # Find the stiffness equation of line between point1 and point2
    # x = np.linspace(x1*0.95, x2*1.05)
    x = xy_data[:, 0]

    # Equation of the line:
    y = y2 + (y2 - y1) / (x2 - x1) * (x - x2)

    # Now equation of the offset
    y_offset = y2 + (y2 - y1) / (x2 - x1) * (x - x2 - offset * x)

    # Finding the yield point: Intersection of y_offset with xy_data
    yield_index = np.argwhere(np.diff(np.sign(xy_data[:, 1] - y_offset))).flatten()
    y_yield = xy_data[yield_index[0]][1]
    x_yield = xy_data[yield_index[0]][0]

    yield_point = Point(x_yield, y_yield)

    return x, y, y_offset, yield_point


def find_ultimate_point(xy_data):
    """ This function returns the maximum of the xy-data """

    # Extracting y-data from xy-data
    y_data = xy_data[:, 1]

    # Finding the index of the maximum value
    ultimate_index = np.argmax(y_data)

    # Locating the ultimate point
    x = xy_data[ultimate_index][0]
    y = xy_data[ultimate_index][1]
    ultimate_point = Point(x, y)

    return ultimate_point


def full_analysis(card):
    # First read the filename from input card
    xy_data_filename = card.filename

    # Extract info: x-title, y-title and xy_data for visualizations
    x_title, y_title, xy_data = extract_xy_data(xy_data_filename)

    # Calculate stiffness
    point1, point2, stiffness = calculate_stiffness(xy_data, card.x1, card.x2)

    # Calculate yield and corresponding point on the xy_data
    yield_point = calculate_yield_point(xy_data, card.offset, point1, point2)

    # Calculate ultimate and corresponding point on the xy_data
    ultimate_point = find_ultimate_point(xy_data)

    # Put all the data into a class containing visualization data
    analysis_output = AnalysisOutput(xy_data, x_title, y_title, stiffness,
                                     point1, point2, yield_point, ultimate_point,
                                     card.offset)

    return analysis_output
