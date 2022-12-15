from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle
from keras_preprocessing.text import tokenizer_from_json
import numpy as np
from IPython.display import clear_output

model = load_model("model")
with open("tokenizer.pickle","rb") as handle:
    tokenizer = pickle.load(handle)
    tokenizer = tokenizer_from_json(tokenizer)

def predict(text):
    if not isinstance(text,list):
        text = [text]
    text = tokenizer.texts_to_sequences(text)
    text = pad_sequences(text, maxlen=28, dtype="int32", value=0)
    result = model.predict(text,batch_size = 1, verbose = 2)[0]
    return "positive" if np.argmax(result) == 1 else "negative" 