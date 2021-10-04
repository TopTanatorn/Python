import mnist
from matplotlib import pyplot as plt
X_train = mnist.train_images()
y_train = mnist.train_labels()
for i in range(30):
    plt.subplot(6,5,i+1)
    plt.title(y_train[i])
    plt.imshow(X_train[i])