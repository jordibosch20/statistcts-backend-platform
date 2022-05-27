import os
from parseInput import parseInput
import numpy as np
from scipy.stats import f_oneway
import tempfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pingouin as pg
# matplotlib.use('Agg')


class Anova():

    def __init__(self, list):
        self.geek = "GeekforGeeks"
        self.data = self.preprocess(list)
        self.checkNormality()

    def preprocess(self, list):
        data_boxplot = []
        for treatment in list:
            data_boxplot.append(treatment)
        treatments = []
        for counter, treatment in enumerate(list):
            treatments = treatments + \
                ['Treatment' + str(counter + 1)]*len(treatment)
        flat_list = [item for sublist in list for item in sublist]
        data = pd.DataFrame(
            {'Treatments': treatments, 'Quantitative Variable': flat_list})
        return data

    def generateBoxPlot(self):
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        sns.boxplot(x="Treatments", y="Quantitative Variable",
                    data=self.data, ax=ax)
        sns.swarmplot(x="Treatments", y="Quantitative Variable",
                      data=self.data, color='black', alpha=0.5, ax=ax)
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        plt.savefig(tmpdir + '/anova.png')

    def checkNormality(self):
        print(pg.normality(data=self.data,
                           dv='Quantitative Variable', group='Treatments'))
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        plt.show()
