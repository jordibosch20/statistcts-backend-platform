import os
from parseInput import parseInput
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
        treatments = []
        for counter, treatment in enumerate(list):
            treatments = treatments + \
                ['Treatment' + str(counter + 1)]*len(treatment)
        flat_list = [item for sublist in list for item in sublist]
        datos = pd.DataFrame(
            {'Treatments': treatments, 'Quantitative Variable': flat_list})
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        sns.boxplot(x="Treatments", y="Quantitative Variable",
                    data=datos, ax=ax)
        sns.swarmplot(x="Treatments", y="Quantitative Variable",
                      data=datos, color='black', alpha=0.5, ax=ax)
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        plt.savefig(tmpdir + '/anova.png')
