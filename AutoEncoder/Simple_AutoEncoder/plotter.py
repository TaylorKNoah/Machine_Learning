import matplotlib.pyplot as plt

class Plotter:
  def __init__(self):
     return
  
  def plotAutoEncoderImages(self, test_imgs, encoded_imgs, decoded_imgs):
    n = 10  # How many digits we will display
    plt.figure(figsize=(10, 2))

    for i in range(n):
        # Display original
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(test_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display Encodings
        ax = plt.subplot(3, n, i + 1 + n)
        plt.imshow(encoded_imgs[i].reshape(2, 1))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(3, n, i + 1 + 2*n)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.show()