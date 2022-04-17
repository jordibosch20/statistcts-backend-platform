import numpy as np
from scipy.stats import f_oneway
import tempfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def generateBoxPlot(list):
    data_boxplot = []
    for treatment in list:
        data_boxplot.append(treatment)
    plt.boxplot(data_boxplot)
    plt.title("Boxplot")
    tmpdir = tempfile.gettempdir()
    print('tmp dir inside anova', tmpdir)
    plt.savefig(tmpdir + '/anova.png')
    generateAnova(list)


def generateAnova(list):
    data = [['Between Groups', '', '', '', '', '', ''], [
        'Within Groups', '', '', '', '', '', ''], ['Total', '', '', '', '', '', '']]
    anova_table = pd.DataFrame(
        data, columns=['Source of Variation', 'SS', 'df', 'MS', 'F', 'P-value', 'F crit'])
    anova_table.set_index('Source of Variation', inplace=True)
    df = pd.DataFrame(list)
    print('df is', df)
    # calculate SSTR and update anova table


def computePValue(list):
    from scipy.stats import f_oneway
    # perform one-way ANOVA
    print(f_oneway(*list))
