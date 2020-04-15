import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from keras.preprocessing.text import tokenizer_from_json
from predictor import LyricsModelPredictor

app = Flask(__name__)
socketio = SocketIO(app)

def create_predictor():
    return LyricsModelPredictor(os.environ['MODEL_PATH'])

def create_tokenizer():
    token_file = open(os.environ['TOKENIZER_JSON_PATH'], 'r')
    train_tokenizer =tokenizer_from_json(token_file.read())
    return train_tokenizer

predictor = create_predictor()
tokenizer = create_tokenizer()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict')
def predict():
    seed_text = request.args.get('seed')
    num_gen = int(request.args.get('num'))
    seed_sequence = tokenizer.texts_to_sequences([seed_text])[0]

    gen_seq = predictor.generate_sequence(seed_sequence, num_gen)
    gen_text = tokenizer.sequences_to_texts([gen_seq])[0]
    return jsonify({'generated_text': gen_text})

@socketio.on('predict')
def async_predict(seed_text, num_gen, reply_topic_id):
    seed_sequence = tokenizer.texts_to_sequences([seed_text])[0]
    output_seq = []
    input_seq = list(seed_sequence)

    for i in range(num_gen):
        predicted = predictor.predict_single(input_seq)
        output_seq.append(predicted)
        input_seq.append(predicted)

        gen_word = tokenizer.index_word[predicted]
        emit(reply_topic_id, { 'word': gen_word, 'seq': i })


