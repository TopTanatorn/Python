from matplotlib import pyplot as plt
from sklearn import datasets
dataset = datasets.load_digits()
print(dataset.keys())
print(dataset.images.shape)
plt.imshow(dataset.images[0])
plt.show()