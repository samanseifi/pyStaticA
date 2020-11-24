# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""

import parser
import analysis
import reportmaker

import sys

if __name__ == "__main__":

    # Step 0: Read the file from command line!
    filename = sys.argv[-1]
    print("Loading", filename, "...")

    # Step 1: Parsing the input file
    # Should be a list of cards with inputs and the reporting style
    input_cards = parser.parse(filename)

    # Step 2: Run analysis over on input data
    # Loop over input cards and list the results for report making
    list_results = []
    for card in input_cards:
        output_result = analysis.full_analysis(card)
        list_results.append(output_result)

    print(list_results[0])
    # Step 3: Create a gorgeous report!
    # Generate the report based on result list
    reportmaker.make_full_report(list_results)
