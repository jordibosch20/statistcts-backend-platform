import scipy.stats as stats
import numpy as np
from flask_restful import Resource


class TTest():
    # methods go here
    def get(self):
        return {'algorithm': 't-test'}, 200  # return data and 200 OK code

    def generateStatistics(tTestValues):
        group1 = np.array(tTestValues[0])
        group2 = np.array(tTestValues[1])

        # perform two sample t-test with equal variances
        statistic, pvalue = stats.ttest_ind(
            a=group1, b=group2, equal_var=False)
        return (statistic, pvalue)