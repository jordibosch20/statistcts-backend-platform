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
from scipy.stats import ks_2samp
matplotlib.use('Agg')


class KolmogorovSmirnov(ParseInput):

    def __init__(self, list):
        super().__init__(list)

    def computeKolmogorovSmirnov(self):
        ks = ks_2samp(
            self.data.loc[self.data.Treatments ==
                          'Treatment1']['Quantitative Variable'],
            self.data.loc[self.data.Treatments ==
                          'Treatment2']['Quantitative Variable']
        )
        print(type(ks))
        return ks
