def mapColumnNames(colName):
    if(colName == 'pval'):
        return 'P Value'
    if(colName == 'equal_var'):
        return 'Equal Variance'
    if(colName == 'SS'):
        return 'SS (Sum of Squares)'
    if(colName == 'SS'):
        return 'SS (Sum of Squares)'
    if(colName == 'DF'):
        return 'DF (Degrees of freedom)'
    if(colName == 'W'):
        return 'W Statistic'
    if(colName == 'F'):
        return 'F Statistic'
    if(colName == 'MS'):
        return 'MS (Mean Sum of Squares)'
    if(colName == 'p-unc'):
        return 'Uncorrected p-values'
    if(colName == 'np2'):
        return 'Partial Eta Squared'
    if(colName == 'normal'):
        return 'Is Normal'
    return colName