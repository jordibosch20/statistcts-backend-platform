from parseInput import ParseInput
import scipy.stats as stats
import numpy as np
import tempfile
import seaborn as sns
import math
from shared import mapColumnNames
import pingouin as pg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


class TTest(ParseInput):

    def __init__(self, list):
        super().__init__(list)

    def computeTTest(self):
        firstGroup = self.data.loc[self.data.Treatments ==
                                   'Treatment1']['Quantitative Variable']
        secondGroup = self.data.loc[self.data.Treatments ==
                                    'Treatment2']['Quantitative Variable']
        ttest = pg.ttest(x=firstGroup, y=secondGroup,
                         alternative='two-sided', paired=True, correction=False)
        columnsNames = ttest.columns.values.tolist()
        columnsNames = map(mapColumnNames, columnsNames)
        columnsNames = list(columnsNames)
        values = ttest.to_numpy().tolist()
        del values[0][4]
        del columnsNames[4]
        return [columnsNames, values]
