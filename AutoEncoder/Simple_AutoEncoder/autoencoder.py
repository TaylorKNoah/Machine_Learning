import keras
from keras import layers

class AutoEncoder:
    def __init__(self):
        self.history = None;
        self.encoded_imgs = None;
        self.decoded_imgs = None;

        self.encoding_dim = 2;
        self.input_img = keras.Input(shape=(784,))

        encoding = layers.Dense(256, activation='relu')(self.input_img)
        encoding = layers.Dense(64, activation='relu')(encoding)
        encoding = layers.Dense(16, activation='relu')(encoding)
        self.encodings = layers.Dense(self.encoding_dim, activation='relu')(encoding)

        decoding = layers.Dense(16, activation='relu')(self.encodings)
        decoding = layers.Dense(64, activation='relu')(decoding)
        decoding = layers.Dense(256, activation='relu')(decoding)
        self.decodings = layers.Dense(784, activation='sigmoid')(decoding)

        self.autoencoder = keras.Model(self.input_img, self.decodings)
        self.autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

        self.encoder = keras.Model(self.input_img, self.encodings)
        self.decoder = keras.Model(self.encodings, self.decodings)

    def trainAndTest(self, train_data, test_data):
        self.history = self.autoencoder.fit(train_data, train_data, epochs=2, batch_size=256, shuffle=True, validation_data=(test_data, test_data))
        self.encoded_imgs = self.encoder.predict(test_data)
        self.decoded_imgs = self.decoder.predict(self.encoded_imgs)

        self.save();

    def save(self):
        return;