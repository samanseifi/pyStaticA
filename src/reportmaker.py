# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""
from plotting import Plotter
import numpy as np


def make_full_report(list_output_results):
    list_ultimate_points = []
    list_yield_points = []
    list_stiffness = []

    # Creating subsequent force displacement curves
    for i in range(0, len(list_output_results)):
        plots = Plotter(list_output_results[i], "plot" + str(i))
        plots.plot_xy_data(r"Rotation $\theta$ ($deg$)", r"Torque ($Nm$)")

        # storing the ultimates (maximum) and offset yields
        list_ultimate_points.append(list_output_results[i].ultimate_point.y)
        list_yield_points.append(list_output_results[i].yield_point.y)
        list_stiffness.append(list_output_results[i].stiffness)

    mean_ultimate = np.mean(np.asarray(list_ultimate_points))
    mean_yield = np.mean(np.asarray(list_yield_points))

    std_ultimate = np.std(np.asarray(list_ultimate_points))
    std_yield = np.std(np.asarray(list_yield_points))
    
    print("mean of ultimates = ", mean_ultimate)
    print("mean of yields = ", mean_yield)

    return "done"


