import numpy as np
import numpy.random

def create_random_data(minx, maxy, a, b, n):
#n is the number of points we create
  x = np.random.normal()
  y = a*x+b+ np.random.normal(size=n)
  return x, y
def consign_excel(datax, datay):
