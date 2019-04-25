import spacy

from jollyjumper.core import get_enjambment
from jollyjumper.rules import get_link_enjambment
from jollyjumper.rules import get_sirrematic_enjambment
from jollyjumper.rules import get_sirrematic_orational_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_prep_before_noun_or_adjective_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_without_de_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_conjunction_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_determiners_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_preposition_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_verbs_enjambment
from jollyjumper.rules import get_sirrematic_with_verb_enjambment

nlp = spacy.load('es_core_news_md')

def test_get_sirrematic_enjambment_ADJ_NOUN():
    text = nlp("verde casa")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADJ', 'NOUN']


def test_get_sirrematic_enjambment_ADV_NOUN():
    text = nlp("malamente casa")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADV', 'NOUN']


def test_get_sirrematic_enjambment_ADP_ADJ():
    text = nlp("con verde")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADP', 'ADJ']


def test_get_sirrematic_enjambment_ADP_NOUN():
    text = nlp("con casa")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADP', 'NOUN']


def test_get_sirrematic_enjambment_ADJ_ADV():
    text = nlp("verde malamente")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADV', 'VERB']


def test_get_sirrematic_enjambment_ADV_VERB():
    text = nlp("vende malamente")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADV', 'VERB']


def test_get_sirrematic_relation_words_preposition_enjambment():
    text = nlp("con cosas")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['ADP', 'NOUN']


def test_get_sirrematic_relation_words_conjunction_enjambment():
    text = nlp("y cosas")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['CONJ', 'NOUN']


def test_get_sirrematic_relation_words_determiners_enjambment_DET_NOUN():
    text = nlp("mis cosas")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['DET', 'NOUN']


def test_get_sirrematic_relation_words_determiners_enjambment_DET_ADJ():
    text = nlp("mis verdes")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['DET', 'ADJ']


def test_get_sirrematic_relation_words_determiners_enjambment_DET_ADV():
    text = nlp("mis malamente")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['DET', 'ADV']


def test_get_sirrematic_relation_words_determiners_enjambment_DET_DET():
    text = nlp("mis mi")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token, next_token) == ['DET', 'DET']


def test_get_sirrematic_with_verb_enjambment_AUX_VERB():
    text = nlp("ha hecho")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_with_verb_enjambment(previous_token, next_token) == ['AUX', 'VERB']


def test_get_sirrematic_with_verb_enjambment_VERB_VERB():
    text = nlp("comer comiendo")
    previous_token = text[0]
    next_token = text[1]
    assert get_sirrematic_with_verb_enjambment(previous_token, next_token) == ['AUX', 'VERB']
