import numpy as np

def get_start_words(trans_mat, n_preds: int):
    first_w_array = trans_mat[0] 
    return argmax(first_w_array, n_preds)

def argmax(arr, k):
    # arr is a 1d numpy array.
    return np.argsort(arr)[::-1][:k].to_list()

