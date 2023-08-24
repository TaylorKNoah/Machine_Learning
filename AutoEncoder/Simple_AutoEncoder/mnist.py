from keras.datasets import fashion_mnist
import numpy as np

class Mnist:
  def __init__(self):
    return
  
  def loadFashionData(self, noisy=False):
    (x_train, _), (x_test, _) = fashion_mnist.load_data()
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

    return x_train, x_test