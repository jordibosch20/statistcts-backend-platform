from parseInput import parseInput
from flask_restful import Resource, reqparse
from flask import request
import numpy as np
from scipy.stats import f_oneway
import tempfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


class Anova():
    def generateBoxPlot(list):
        data_boxplot = []
        for treatment in list:
            data_boxplot.append(treatment)
        plt.boxplot(data_boxplot)
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        plt.savefig(tmpdir + '/anova.png')

    def computePValue(list):
        from scipy.stats import f_oneway
        # perform one-way ANOVA
        print(f_oneway(*list))
