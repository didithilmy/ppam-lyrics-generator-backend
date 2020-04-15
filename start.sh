#!/bin/bash
MODEL_PATH="/home/ubuntu/ml/lyrics_model.h5"
TOKENIZER_JSON_PATH="/home/ubuntu/ml/tokenizer_dict.json"

MODEL_PATH=$MODEL_PATH TOKENIZER_JSON_PATH=$TOKENIZER_JSON_PATH gunicorn -w 1 -b 0.0.0.0:8080 --chdir ppam-lyrics-generator-backend/ app:app
