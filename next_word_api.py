from flask import Flask, request
import pickle
import json
from utils import get_start_words, argmax

app = Flask(__name__)

N_START_WORDS = 10

# Load the object from the file
with open('prob_mat.pkl', 'rb') as f:
    trans_mat = pickle.load(f)

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def predict_next_word(word: str, n_preds: int):
    word_token = tokenizer.get_index(word)
    next_token_probs = trans_mat[word_token]
    token_list = argmax(next_token_probs, n_preds)
    words = [tokenizer.get_word(word_token) for word_token in token_list]
    return words 

def prompt_user():
    start_words = get_start_words(trans_mat, N_START_WORDS)
    start_words = [tokenizer.get_word(word) for word in start_words]
    sen = list()
    for i, word in enumerate(start_words):
        print(f"{i} -- {word}  ")

    while True:
        selected_idx = int(input("Choose a number.\n"))
        selected_word = start_words[selected_idx]
        sen.append(selected_word)
        if selected_word == "<end>":
            print(" ".join(sen))
            break 
        start_words = predict_next_word(selected_word, N_START_WORDS)
        print("next found: ", start_words)
        #start_words = [tokenizer.get_word(word) for word in start_words]
        for i, word in enumerate(start_words):
            print(f"{i} -- {word}  ")

@app.route('/get-next-words/', methods=['POST'])
def get_next_words():
    word = request.json.get("word")

    if word == "<start>":
        start_words = get_start_words(trans_mat, N_START_WORDS)
        start_words = [tokenizer.get_word(word) for word in start_words]
        response = {"next_words": start_words}
    else:
        next_word_preds = predict_next_word(word, N_START_WORDS)
        response = {"next_words": next_word_preds}
        
    return json.dumps(response), 200

if __name__=="__main__":
    #prompt_user(port=5000) 
    app.run(port=5000)