import numpy as np
import sys
import pickle
from utils import get_start_words, argmax
from tokenizer import Tokenizer

#np.set_printoptions(threshold=sys.maxsize)
# Load the sentences first.
DATASET_PATH =  "corpus_nepali/translated.txt"
in_file = open(DATASET_PATH, "r")


END_TOKEN = "<end>"
sentences = list()

vocab_set = set()
vocab_set.add(END_TOKEN)

start_word_dict = dict()
freq_dict = dict()


for line in in_file:
    line = line.replace("?", "")
    line = line.replace("।", "")
    line = line.replace(",", "")
    line = line.replace("\n", "")
    sentences.append(line)
    words = line.split(" ")
    for word in words:
        vocab_set.add(word)

tokenizer = Tokenizer(vocab_set)
N_WORDS = len(vocab_set)
print(N_WORDS)

# create transition probability matrix
trans_mat = np.zeros([N_WORDS, N_WORDS])

freq_dict[END_TOKEN] = len(sentences)
for sen in sentences:
    words = sen.split(" ")
    n_words = len(words)
    for i, word in enumerate(words):
        if i == 0:
            if word in start_word_dict.keys():
                start_word_dict[word] = start_word_dict[word] + 1
            else:
                start_word_dict[word] = 1
        idx = tokenizer.get_index(word)
        if i != n_words - 1:
            nxt_word = words[i+1]
        else:
            nxt_word = END_TOKEN
        
        if word in freq_dict.keys():
            freq_dict[word] = freq_dict[word] + 1
        else:
            freq_dict[word] = 1
        
        nxt_idx = tokenizer.get_index(nxt_word)
        trans_mat[idx][nxt_idx] = trans_mat[idx][nxt_idx] + 1

# normalize the transition freq matrix
trans_mat = trans_mat.astype(float)
for idx in range(N_WORDS):
    word = tokenizer.get_word(idx)
    word_freq = freq_dict[word]
    trans_mat[idx, :] = trans_mat[idx, :] / word_freq

# save trans_mat to .pkl
with open('prob_mat.pkl', 'wb') as f:
    pickle.dump(trans_mat, f)

# save tokenizer to .pkl
with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

#print(freq_dict)
#print(type(trans_mat))
print(trans_mat.shape)

#close the file at the end..
in_file.close()



if __name__=="__main__":
    print("Generating some names:")

    #start_words = get_start_words(10)
    #print(start_words)