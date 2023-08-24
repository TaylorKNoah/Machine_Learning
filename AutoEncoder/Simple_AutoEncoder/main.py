from autoencoder import AutoEncoder
from mnist import Mnist
from plotter import Plotter

mnist = Mnist();
autoencoder = AutoEncoder();
pyplotter = Plotter();

train_data, test_data = mnist.loadFashionData(noisy=True);
autoencoder.trainAndTest(train_data, test_data);
pyplotter.plotAutoEncoderImages(test_imgs=test_data, encoded_imgs=autoencoder.encoded_imgs, decoded_imgs=autoencoder.decoded_imgs)