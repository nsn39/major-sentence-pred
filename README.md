# Markov Chain Text Prediction

This project uses a Markov Chain model to predict the next word in a sentence. The project consists of two main scripts: `markov_chain.py` and `next_word_api.py`.

## Getting Started

To get started, you need to run the `markov_chain.py` script to create two pickle files, `prob_mat.pkl` and `tokenizer.pkl`. These files will be used by the `next_word_api.py` script to make predictions.

```
python markov_chain.py
```

Once the pickle files are created, you can start the API endpoint by running the next_word_api.py script:

```
python next_word_api.py
```

The API will be running on http://localhost:5000/get-next-words and accepts POST requests with a request body containing the parameter sentence. The response will be a JSON object with a key next_words corresponding to a list of ten different predictions for the next word.