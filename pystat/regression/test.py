import pandas as pd
import numpy as np
import unittest

from pystat.regression.linear import LinearRegression


class LinearRegressionTest(unittest.TestCase):
	def test_corr(self):
		data = pd.read_csv('../dataset/math-score-drug-concentration.csv')
		ln = LinearRegression(data['x'], data['y'])
		ln.correlation()
		self.assertAlmostEqual(ln.corr, 0.99, places=2)


if __name__ == '__main__':
	unittest.main()
