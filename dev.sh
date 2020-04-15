#!/bin/bash
MODEL_PATH="/home/ubuntu/ml/lyrics_model.h5"
TOKENIZER_JSON_PATH="/home/ubuntu/ml/tokenizer_dict.json"
FLASK_APP="/home/ubuntu/app/ppam-lyrics-generator-backend/app.py"

MODEL_PATH=$MODEL_PATH TOKENIZER_JSON_PATH=$TOKENIZER_JSON_PATH FLASK_APP=$FLASK_APP python -m flask run --host=0.0.0.0 -p 5000
