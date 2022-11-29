import matplotlib.pyplot as plt

def generate():
  labels = ['a','b','c']
  values = [100,200,300]
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

if __name__ == '__main__':
  generate()
  