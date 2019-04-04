#!/usr/bin/python
# Rules are based on previous work from Pablo Ruiz
# https://github.com/postdataproject/skas-archived/blob/devel/skas/phonmet/syll/grapheme2syllable.py

import re
import spacy

nlp = spacy.load('es_core_news_md')
alphanumeric = re.compile("[a-z0-9]")
alpha = re.compile("[a-z]")

text = """El año 2000
-a la luz de un candil-
los supervivientes
no vean más plan,
que un terrible llan-
to y crujir de dientes
bellos se puede apostar,
sin menospreciar
a aquellos profetas,
que aseguran que,
el remedio viene
de otros planetas
malamente pero ok"""

text2 = """que un terrible llan-
to y crujir de bellos
dientes se puede apostar."""

text3 = """el remedio vie-
ne de otros planetas
malamente pero ok"""


def remove_whitespaces(poem):
    """
    Removes '\r' '\t' '\n' from a poem, or any combination of them
    :param poem:
    :return:
    """
    clean_poem = re.sub('[\n\r\t]+', ' ', poem)
    nlp_clean_poem = []
    nlp_raw_poem = []
    rebuilt_poem = []
    for token_clean_poem in nlp(clean_poem):
        nlp_clean_poem.append(token_clean_poem)
    for token_raw_poem in nlp(poem):
        nlp_raw_poem.append(token_raw_poem)
    while nlp_raw_poem:
        token_raw = nlp_raw_poem.pop()
        if token_raw.pos_ != 'SPACE':
            rebuilt_poem.append(nlp_clean_poem.pop())
        else:
            rebuilt_poem.append(token_raw)
    rebuilt_poem.reverse()
    return rebuilt_poem


def has_tmesis(previous_token, next_token):
    """
    Checks if tmesis exists between two verses
    :param previous_token: The word before a newline character
    :param next_token: The word after a newline character
    :return:
    """
    if previous_token.text[-1] == '-':
        print("Encabalgamiento: Tmesis de '" + previous_token.text + "' con '" + next_token.text + "'")


def has_sirrematic_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two verses
    :param previous_token: The word before a newline character
    :param next_token: The word after a newline character
    :param pos_pair:
    :return:
    """
    sirremactic_pairs = [['ADJ', 'NOUN'],
                         ['ADV', 'NOUN'],
                         ['ADP', 'ADJ'],
                         ['ADP', 'NOUN'],
                         ['ADJ', 'ADV'],
                         ['ADV', 'VERB']
                         ]
    while sirremactic_pairs:
        if sorted((previous_token.pos_, next_token.pos_)) == sorted(sirremactic_pairs.pop())\
                and (next_token.is_ancestor(previous_token) or previous_token.is_ancestor(next_token))\
                and previous_token.text[-1] != '-':
                print("Encabalgamiento: Sirremático " + previous_token.pos_ + "+" + next_token.pos_ + " de " + previous_token.text + " con " + next_token.text)


def get_enjambment(original_poem):
    """
    Scan a text for all possible enjambment types.
    :param original_poem:
    :return:
    """
    nlp_poem = remove_whitespaces(original_poem)
    #for w in nlp_poem:
    #    print(w.text, w.pos_)
    # We iterate through all the text up to the penultimate line
    for i, token in enumerate(nlp_poem[:-1]):
        previous_token = nlp_poem[i - 1]
        next_token = nlp_poem[i + 1]
        # print(token.lemma_, token.pos_, token.text)
        # We look for enjambment when if there are words before and after a newline character
        if token.text[-1] == '\n' and not previous_token.is_punct and not next_token.is_punct:
            # print(previous_token.text, previous_token.pos_, next_token.text, next_token.pos_)
            has_tmesis(previous_token, next_token)
            has_sirrematic_enjambment(previous_token, next_token)
