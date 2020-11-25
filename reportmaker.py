# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:57:28 2019

@author: Saman Seifi, PhD
@company: DePuy Synthes
"""
from plotting import Plotter


def make_full_report(list_results):
    # Creating subsequent force displacement curves
    for i in range(0, len(list_results)):
        plots = Plotter(list_results[i], "plot" + str(i))
        plots.plot_xy_data(r"Rotation $\theta$ ($deg$)", r"Torque ($Nm$)")

    return "done"
