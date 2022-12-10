import pandas as pd
import numpy as np
def access_data(file_name, extension):
  #the data in textfile is such that we have two columns the x and the y
  if extension is None:
    extension=file_name.split('.')[-1]
    print("We will extract data from file", file_name, " with extension ", extension)
  if extension=='.txt':
    with open(file_name) as f:
      lines=f.readlines()
    datax = []
    datay = []
    for line in lines:
      x, y = line.split()
      x, y=float(x), float(y)
      datax.append(x)
      datay.append(y)
  elif extension=='xlsx':
    df = pd.read_excel('sample.xlsx')
    datax = df[:, 0]
    datax = df[:, 1]
  else:
    raise Exception("Sorry, unsupported extension") 
  return datax, datay
