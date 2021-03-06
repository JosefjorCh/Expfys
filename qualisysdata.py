import numpy as np
import matplotlib.pyplot as plt

def loadtsv(file):
  """ Reads a tsv file generated by qualisys cameras with headers.
  Returns a list of positions over time """
  n=open(file)
  l = n.readlines()
  n.close()

  for i in range(9):
    l.pop(0)

  l[0]=l[0].split() # Make the first item a list with names of the markers
  l[0].pop(0)

  for i in range(1,len(l)):
    l[i]=[float(e) for e in l[i].split()] # Make all coordinates into floats
    l[i]= [l[i][3*n:3*n+3]  for n in range (int(len(l[i])/3))] # create separate lists for separate markers
    # Each marker has 3 dimensions, x,y,z
  return l


def graph(file, freq, axis="xyz", marker="1"):
  """ Plots each axis over time individually """
  data = loadtsv(file)
  for n in marker:
    j = int(n)-1
    for a in axis:
      i = ord(a)-120 # give "x" a value of 0, "y"-1, "z"-2
      X = np.linspace(0, (len(data)-1)/freq,len(data)-1)
      Y = [e[j][i] for e in data[1:]] # plot coordinate i, marker j
      plt.plot(X,Y)

  plt.show()
