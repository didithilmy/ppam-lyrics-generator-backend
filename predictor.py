from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
import numpy as np

class LyricsModelPredictor:
    def __init__(self, model_file_path):
        self.max_vocabulary_size = 9000
        self.n_steps = 10
        self.model = keras.models.load_model(model_file_path)
        print("Model loaded")
        print(self.model.summary())

    def predict_single(self, input_sequence):
        pad_encoded = pad_sequences([input_sequence], maxlen=self.n_steps, truncating='pre')
        pad_encoded = np.reshape(pad_encoded, (1, self.n_steps, 1))
        pad_encoded = pad_encoded / float(self.max_vocabulary_size)
        pred_word_ind = self.model.predict_classes(pad_encoded, verbose=0)[0]
        return int(pred_word_ind)

    def generate_sequence(self, seed_sequence, num_words):
        output_seq = []
        input_seq = list(seed_sequence)

        for i in range(num_words):
            predicted = self.predict_single(input_seq)
            output_seq.append(predicted)
            input_seq.append(predicted)

        return output_seq

