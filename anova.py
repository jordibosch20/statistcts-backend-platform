import os
from parseInput import ParseInput
from shared import mapColumnNames
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pingouin as pg
import math
matplotlib.use('Agg')


class Anova(ParseInput):

    def __init__(self, list):
        super().__init__(list)

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
