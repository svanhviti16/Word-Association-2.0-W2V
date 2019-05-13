# Backend for a word association game by Svanhvít Lilja Ingólfsdóttir
# word2vec model is given as first command line argument (.model file)
# ex.: 
# $ python3 api.py WV_RMH/RMH2_w2v.model


import requests
import responder
import sys
from urllib.parse import unquote
from gensim.models import Word2Vec
from gensim import models
import codecs
import random


def load_model():
    model_file = sys.argv[1] 
    model = Word2Vec.load(model_file)
    return model

word_list = [ "ostur", "forseti", "tónlist", "klukka", "gluggi", "peysa", "Ísland", "tennis", "tölva", "sígaretta", "sauðfjárbændur", "haust",
            "Reykjavík", "súkkulaði", "skóli", "kerti", "grænmeti", "jól", "bíll", "hundur", "skip", "dauði", "Bandaríkin", "kosningar", "Færeyjar",
            "vinna", "læknir", "gleraugu", "kjóll", "bíómynd", "sjónvarp", "fótbolti", "mús", "stjórnmál", "Laddi", "femínistar", "Ísafjörður", 
            "kennari", "sundlaug", "krá", "bjór", "sumarfrí", "verðlaun", "auga", "ljótur", "sætur", "illska", "veikindi", "sjór", 
            "HÍ", "skyr", "trúður", "hamborgari", "Eiður", "svartur", "Facebook", "Eurovision", "Köben", "tíska", "brandari", "Sódóma", "Sjálfstæðisflokkurinn",
            "rokk", "hjarta", "kvef", "gítar", "Bjöggi", "Megas", "Vigdís", "Madonna", "kanína", "Öskjuhlíð", "Laugavegur", "einkabíll", "grilla",
            "Morthens", "hákarl", "útrásarvíkingur", "plokkfiskur", "fíll", "Stuðmenn", "próf", "iPhone", "sjómenn", "gluggaveður", "hálfviti", "líf", 
            "afmæli", "Obama", "djamm", "Bítlarnir", "te", "sjúklega", "Bjarnfreðarson", "kex", "mjór", "feitur", "veiðiferð", "meðferð", "bólusetningar" ]

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
    else:
        answer = False
    resp.media = {'is_correct': answer, 'most_similar' : most_similar_to_input}

if __name__ == '__main__':
    api.run()

