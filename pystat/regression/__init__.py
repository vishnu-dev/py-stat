from abc import ABC, abstractmethod


class Regression(ABC):
	
	@abstractmethod
	def predict(self, z):
		pass
	
	@abstractmethod
	def fit(self, x, y):
		pass

