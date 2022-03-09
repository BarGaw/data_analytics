import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#1
plik_1 = pd.read_csv("Data1.csv", index_col=0)

def analysis(plik):
    #2
    print(plik.head())

    #3
    plik.plot()
    plt.show()

    #4
    plik.hist(bins=len(plik.theta_1.unique())//100)
    plt.show()

    #5
    plik.plot.kde()
    plt.show()

analysis(plik_1)
#6
analysis(plik_1.loc['2018-01-01':'2018-12-12'])