import pickle
from utils import get_start_words, argmax

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

if __name__=="__main__":
    prompt_user() 