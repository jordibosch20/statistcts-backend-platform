import os
from parseInput import parseInput
from shared import mapColumnNames
import numpy as np
from scipy.stats import f_oneway
import tempfile
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pingouin as pg
import math
matplotlib.use('Agg')


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
        self.numberTreatments = counter + 1
        flat_list = [item for sublist in list for item in sublist]
        data = pd.DataFrame(
            {'Treatments': treatments, 'Quantitative Variable': flat_list})
        return data

    def generateBoxPlot(self):
        fig, ax = plt.subplots(1, 1, figsize=(7, 4))
        sns.boxplot(x="Treatments", y="Quantitative Variable",
                    data=self.data, ax=ax)
        sns.swarmplot(x="Treatments", y="Quantitative Variable",
                      data=self.data, color='black', alpha=0.5, ax=ax)
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        plt.savefig(tmpdir + '/anova.png')

    def checkNormality(self):
        plt.title("Boxplot")
        tmpdir = tempfile.gettempdir()
        numberRows = math.ceil(self.numberTreatments / 2)
        fig, axs = plt.subplots(numberRows, 2, figsize=(8, 6))
        if(self.numberTreatments % 2 == 0):
            for i in range(0, numberRows):
                pg.qqplot(self.data.loc[self.data.Treatments ==
                                        'Treatment' + str(2*i + 1), 'Quantitative Variable'], dist='norm', ax=axs[i, 0])
                axs[i, 0].set_title('Treatment' + str(2*i + 1))
                pg.qqplot(self.data.loc[self.data.Treatments ==
                                        'Treatment' + str(2*i + 2), 'Quantitative Variable'], dist='norm', ax=axs[i, 1])
                axs[i, 1].set_title('Treatment' + str(2*i + 2))
            plt.tight_layout()
        else:
            for i in range(0, numberRows - 1):
                pg.qqplot(self.data.loc[self.data.Treatments ==
                                        'Treatment' + str(2*i + 1), 'Quantitative Variable'], dist='norm', ax=axs[i, 0])
                axs[i, 0].set_title('Treatment' + str(2*i + 1))
                pg.qqplot(self.data.loc[self.data.Treatments ==
                                        'Treatment' + str(2*i + 2), 'Quantitative Variable'], dist='norm', ax=axs[i, 1])
                axs[i, 1].set_title('Treatment' + str(2*i + 2))
            pg.qqplot(self.data.loc[self.data.Treatments ==
                                    'Treatment' + str(2 * numberRows - 1), 'Quantitative Variable'], dist='norm', ax=axs[numberRows - 1, 0])
            axs[numberRows - 1,
                0].set_title('Treatment' + str(2 * numberRows - 1))
            plt.tight_layout()
        plt.savefig(tmpdir + '/anova2.png')

    def computeNormality(self):
        # Test de normalidad Shapiro-Wilk
        normality = pg.normality(data=self.data, dv='Quantitative Variable',
                                 group='Treatments')
        columnsNames = normality.columns.values.tolist()
        columnsNames = map(mapColumnNames, columnsNames)
        columnsNames = list(columnsNames)
        values = normality.to_numpy().tolist()
        return [columnsNames, values]

    def checkHomocedasticity(self):
        homocedasticity = pg.homoscedasticity(
            data=self.data, dv='Quantitative Variable', group='Treatments', method='levene')
        columnsNames = homocedasticity.columns.values.tolist()
        columnsNames = map(mapColumnNames, columnsNames)
        columnsNames = list(columnsNames)
        values = homocedasticity.to_numpy().tolist()
        return [columnsNames, values]

    def computeAnova(self):
        anova = pg.anova(
            data=self.data, dv='Quantitative Variable', between='Treatments', detailed=True)
        anova = anova.fillna(-1)
        columnsNames = anova.columns.values.tolist()
        columnsNames = map(mapColumnNames, columnsNames)
        columnsNames = list(columnsNames)
        values = anova.to_numpy().tolist()
        return [columnsNames, values]

    def comptueTukey(self):
        tukey = pg.pairwise_tukey(
            data=self.data, dv='Quantitative Variable', between='Treatments').round(3)
        columnsNames = tukey.columns.values.tolist()
        columnsNames = map(mapColumnNames, columnsNames)
        columnsNames = list(columnsNames)
        values = tukey.to_numpy().tolist()
        return [columnsNames, values]
