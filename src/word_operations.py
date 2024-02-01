# word_operations.py
from nltk.corpus import wordnet

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return None

def get_synonyms(word):
    synonyms = set()
    synsets = wordnet.synsets(word)
    for syn in synsets:
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def get_antonyms(word):
    antonyms = set()
    synsets = wordnet.synsets(word)
    for syn in synsets:
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    return list(antonyms)
