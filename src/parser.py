# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""


class AnalysisInput:
    """ This class contains filename of the input data, offset value,
    x1 and x2 points for calculating stiffness"""

    def __init__(self, filename, offset, x1, x2):
        self.filename = filename
        self.offset = float(offset)
        self.x1 = float(x1)
        self.x2 = float(x2)


def line_parser(line):
    """ Take the line (as string) parsed from input file
        Splitting the line into tokens the format should be:
        filename(string) offset(float) x1(float) x2(float) and return as a class"""

    # Splitting line to tokens of filename, offset etc.
    line_tokens = line.split(" ")

    # Create a class
    for token in line_tokens:
        line_input_data = AnalysisInput(line_tokens[0], line_tokens[1], line_tokens[2], line_tokens[3])
    return line_input_data


def parse(filename):
    """ This function returns a list contaning classes where
    the input data are set for analysis """

    # Initialize a list of input data for individual analysis
    analysis_input_card = []

    # Read the input file
    with open(filename, 'r') as file_object:
        lines = file_object.readlines()

        # Append each line of analysis input data to a list
        for line in lines:
            line_input_data = line_parser(line)
            analysis_input_card.append(line_input_data)

    return analysis_input_card
