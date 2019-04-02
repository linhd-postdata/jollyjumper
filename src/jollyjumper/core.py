#!/usr/bin/python
# Rules are based on previous work from Pablo Ruiz
# https://github.com/postdataproject/skas-archived/blob/devel/skas/phonmet/syll/grapheme2syllable.py

import re

import spacy

print("Loading model...")
nlp = spacy.load('es_core_news_md')
alphanumeric = re.compile("[a-z0-9]")

text = nlp("""El año 2000
-a la luz de un candil-
los supervivientes
no vean más plan,
que un terrible llan-
to y crujir de dientes,
se puede apostar,
sin menospreciar
a aquellos profetas,
que aseguran que,
el remedio vie-
ne de otros planetas.
Que bonitos son-""")

def has_tmesis(previous_token, next_token):
    """

    :param previous_token:
    :param next_token:
    :return:
    """
    if previous_token.text[-1] == '-':
        print("Encabalgamiento: Tmesis de " + previous_token.text + " con " + next_token.text)


def get_enjambment(original_poem):
    text = nlp(original_poem)
    for i, token in enumerate(text[:-1]):
        previous_token = text[i - 1]
        next_token = text[i + 1]
        if token.text[-1] == '\n':
            has_tmesis(previous_token, next_token)
