from copy import deepcopy
import math


def mean(X):
  return sum(X)/len(X)

def variance(X):
  return mean([x**2 for x in X])-mean(X)**2
  
class linear_regression:
  def __init__(self, aini, bini):
    self.a = a
    self.b = bini
    self.datax = []
    self.datay = []

  def __init__(self, aini, bini, datainix, datainiy):
    self.a = a
    self.b = bini
    self.datax = deepcopy(datainix)
    self.datay = deepcopy(datainiy)
    
  def __init__(self, datainitx, datainity):
    self.datax = deepcopy(datainitx)
    self.datay = deepcopy(datainity)
    self.compute()
  
  def compute():
      self.a = math.sqrt(variance(self.datay)/variance(self.datax))
      self.b = mean(datay)-self.a*mean(datax)
