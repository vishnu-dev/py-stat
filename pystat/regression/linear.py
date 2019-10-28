from pystat.regression import Regression
import numpy as np


class LinearRegression(Regression):
    """
    Simple Linear Regression - One dependant and One Independent variable
    y = mx + c
    """
    def __init__(self, feature=None, response=None):
        self.y = response
        self.x = feature
        self.m = None
        self.c = None
        self.corr = None

    def predict(self, z):
        pass

    def correlation(self):
        """
        Calculate Correlation Coefficient between two variables
        :return: Value of correlation coefficient that lies between -1 and +1
        """
        self.corr = np.cov(self.x, self.y)[0][1] / (np.std(self.x) * np.std(self.y))

    def fit(self, x, y):

        if x is None:
            raise ValueError('Input values for dependent variable x')
        if y is None:
            raise ValueError('Input values for independent variable y')
        
        self.x = x
        self.y = y
        
        self.correlation()
        
        return self


def test():
    import pandas as pd
    data = pd.read_csv('../dataset/math-score-drug-concentration.csv')
    ln = LinearRegression(data['x'], data['y'])
    ln.correlation()
    print(ln.corr)


if __name__ == '__main__':
    test()

