from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os
import re

savedModel=load_model(os.getcwd()+'/base/static/model/'+'Model.h5')

vocab_size = 20000
oov_tok = "<OOV>"
max_length = 100
padding_type='post'
trunc_type='post'
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)

def start_sentiment(df):
    final_result = list()
    for tweets in df:
        if tweets['description']:
            tt = re.findall('http://\S+|https://\S+', tweets['description'])
            for i in tt:
                tweets['description'] = tweets['description'].replace(i, '')
            test = [str(tweets['description'])]
            tokenizer.fit_on_texts(test)
            test_text = tokenizer.texts_to_sequences(test)
            test_text_padded = pad_sequences(test_text, maxlen=max_length, padding=padding_type, truncating=trunc_type)
            prediction = savedModel.predict(test_text_padded)

            # 0 : bad
            # 1 : good
            tweets['result'] = prediction[0][0]*100
            tweets.pop('retweetcount')
            tweets.pop('totaltweets')
            final_result.append(tweets)
    return final_result

