import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('loansData.csv')

loansData.dropna(inplace=True)

def makeBoxplot(data, col, imgOut):
    plt.figure()
    data.boxplot(column=col)
    plt.savefig(imgOut)

def makeHist(data, col, imgOut):
    plt.figure()
    data.hist(column=col)
    plt.savefig(imgOut)

def makeQQ(data, col, imgOut):
    plt.figure()
    graph = stats.probplot(data[col], dist="norm", plot=plt)
    plt.savefig(imgOut)

colName1 = 'Amount.Funded.By.Investors'

makeBoxplot(loansData, colName1, 'Amount funded boxplot')
makeHist(loansData, colName1, 'Amount funded histogram')
makeQQ(loansData, colName1, 'Amount funded QQ plot')

colName2 = 'Amount.Requested'

makeBoxplot(loansData, colName2, 'Amount requested boxplot')
makeHist(loansData, colName2, 'Amount requested histogram')
makeQQ(loansData, colName2, 'Amount requested QQ plot')