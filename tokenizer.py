class Tokenizer:
    def __init__(self, vocab_set):
        self.vocab_set = vocab_set
        self.word_to_idx = dict()
        for i, item in enumerate(vocab_set):
            self.word_to_idx[item] = i 

    def get_word(self, index):
        r_idx = 0
        for word in self.vocab_set:
            if self.word_to_idx[word] == index:
                r_idx = word
                break
        return r_idx

    def get_index(self, word):
        return self.word_to_idx[word]