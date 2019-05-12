import requests
import responder
import sys
from urllib.parse import unquote
#from reynir.bincompress import BIN_Compressed
from gensim.models import Word2Vec
from gensim import models
import codecs
import random

# python3 api.py data/RMH2_w2v.model data/IS_WN/core-isl.txt 

#beygingarlýsing
#bin = BIN_Compressed()

# word2vec model given as first command line argument
def load_model():
    model_file = sys.argv[1] 
    model = Word2Vec.load(model_file)
    return model

word_list = ["ostur", "forseti", "tónlist", "klukka", "gluggi", "peysa", "Ísland", "tennis", "tölva", "sígaretta",
            "Reykjavík", "súkkulaði", "skóli", "kerti", "grænmeti", "jól", "bíll", "hundur", "skip", "dauði", "Bandaríkin",
            "vinna", "læknir", "gleraugu", "kjóll", "bíómynd", "sjónvarp", "fótbolti", "mús", "stjórnmál", 
             "kennari", "sundlaug", "krá", "bjór", "sumarfrí", "verðlaun"]

model = load_model()

def get_random(words):
    return random.sample(words, k=4)

def get_most_similar(input_word, random_sample):
    try:
        return model.wv.most_similar_to_given(input_word, random_sample)
    except KeyError:
        return None

# setting the header parameters in the constructor
api = responder.API(cors=True, cors_params={'allow_origins':['*']})

@api.route('/words')
def get_word(req, resp):
    words = get_random(word_list)
    resp.media = { 'mainword': words[0], 'otherwords' : words[1:] }


@api.route('/userword/{userword}+{mainword}+{otherwords}')
def is_valid_word(req, resp, *, userword, mainword, otherwords):
    user_word = unquote(userword)
    main_word = unquote(mainword)
    all_words = unquote(otherwords).split(",")
    all_words.append(main_word)
    most_similar_to_input = get_most_similar(user_word, all_words)
    print(f'userword: {user_word}, mainword: {main_word}, most_similar: {most_similar_to_input}, allthewords: {all_words}')
    if main_word == most_similar_to_input:
        answer = True
        print("RÉTT, orðið er " + mainword)
    else:
        answer = False
    resp.media = {'is_correct': answer, 'most_similar' : most_similar_to_input}

if __name__ == '__main__':
    api.run()

