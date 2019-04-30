from unittest import mock

from jollyjumper.rules import get_link_enjambment
from jollyjumper.rules import get_sirrematic_enjambment
from jollyjumper.rules import get_sirrematic_orational_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_before_noun_adjective_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_enjambment
from jollyjumper.rules import get_sirrematic_prepositional_without_de_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_conjunction_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_determiners_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_preposition_enjambment
from jollyjumper.rules import get_sirrematic_relation_words_verbs_enjambment
from jollyjumper.rules import get_sirrematic_with_verb_enjambment


class TokenMock(mock.MagicMock):
    _ = property(lambda self: mock.Mock(has_tmesis=self.has_tmesis,
                                        line=self.line))

    @staticmethod
    def is_ancestor(token):  # noqa
        return True

    @staticmethod
    def nbor():  # noqa
        return TokenMock()


def test_get_sirrematic_enjambment_adj_noun():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(pos_="NOUN")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADJ',
                                                                     'NOUN']


def test_get_sirrematic_enjambment_adv_noun():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(pos_="NOUN")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADV',
                                                                     'NOUN']


def test_get_sirrematic_enjambment_adp_adj():
    previous_token = TokenMock(pos_="ADP")
    next_token = TokenMock(pos_="ADJ")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADP',
                                                                     'ADJ']


def test_get_sirrematic_enjambment_adp_noun():
    previous_token = TokenMock(pos_="ADP")
    next_token = TokenMock(pos_="NOUN")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADP',
                                                                     'NOUN']


def test_get_sirrematic_enjambment_adj_verb():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(pos_="ADV")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADJ',
                                                                     'ADV']


def test_get_sirrematic_enjambment_adv_verb():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(pos_="VERB")
    assert get_sirrematic_enjambment(previous_token, next_token) == ['ADV',
                                                                     'VERB']


def test_get_sirrematic_relation_words_preposition_enjambment_adp_dummy():
    previous_token = TokenMock(lower_="a", pos_="ADP", tag_="AdpType=Prep")
    next_token = TokenMock(pos_="dummy")
    assert get_sirrematic_relation_words_preposition_enjambment(previous_token,
                                                                next_token) == [
               'ADP', 'dummy']


def test_get_sirrematic_relation_words_conjunction_enjambment_conj_dummy():
    previous_token = TokenMock(lower_="a", pos_="CONJ", tag_="AdpType=Prep")
    next_token = TokenMock(pos_="dummy")
    assert get_sirrematic_relation_words_conjunction_enjambment(previous_token,
                                                                next_token) == [
               'CONJ', 'dummy']


def test_get_sirrematic_relation_words_determiners_enjambment_det_noun():
    previous_token = TokenMock(pos_="DET")
    next_token = TokenMock(pos_="NOUN")
    assert get_sirrematic_relation_words_determiners_enjambment(previous_token,
                                                                next_token) == [
               'DET', 'NOUN']


def test_get_sirrematic_relation_words_determiners_enjambment_det_adj():
    previous_token = TokenMock(pos_="DET")
    next_token = TokenMock(pos_="ADJ")
    assert get_sirrematic_relation_words_determiners_enjambment(previous_token,
                                                                next_token) == [
               'DET', 'ADJ']


def test_get_sirrematic_relation_words_determiners_enjambment_det_adv():
    previous_token = TokenMock(pos_="DET")
    next_token = TokenMock(pos_="ADV")
    assert get_sirrematic_relation_words_determiners_enjambment(previous_token,
                                                                next_token) == [
               'DET', 'ADV']


def test_get_sirrematic_relation_words_determiners_enjambment_det_det():
    previous_token = TokenMock(pos_="DET")
    next_token = TokenMock(pos_="DET")
    assert get_sirrematic_relation_words_determiners_enjambment(previous_token,
                                                                next_token) == [
               'DET', 'DET']


def test_get_sirrematic_with_verb_enjambment_aux_verb():
    previous_token = TokenMock(pos_="AUX")
    next_token = TokenMock(pos_="VERB")
    assert get_sirrematic_with_verb_enjambment(previous_token, next_token) == [
        'AUX', 'VERB']


def test_get_sirrematic_with_verb_enjambment_verb_verb():
    previous_token = TokenMock(pos_="VERB")
    next_token = TokenMock(pos_="VERB")
    assert get_sirrematic_with_verb_enjambment(previous_token, next_token) == [
        'VERB', 'VERB']


def test_get_sirrematic_orational_enjambment_adj_que():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="que", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_adj_cuyo():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="cuyo", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_adj_cuya():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="cuya", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_adj_cuyos():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="cuyos", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_adj_cuyas():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="cuyas", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_adj_donde():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="donde", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADJ', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_que():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="que", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_cuyo():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="cuyo", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_cuya():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="cuya", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_cuyos():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="cuyos", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_cuyas():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="cuyas", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_noun_donde():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="donde", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'NOUN', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_que():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="que", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_cuyo():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="cuyo", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_cuya():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="cuyas", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_cuyos():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="cuyos", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_cuyas():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="cuyas", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_orational_enjambment_adv_donde():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="donde", pos_="dummy", tag_="NumType")
    assert get_sirrematic_orational_enjambment(previous_token, next_token) == [
        'ADV', 'dummy']


def test_get_sirrematic_relation_words_verbs_enjambment_none():
    previous_token = TokenMock(pos_="dummy")
    next_token = TokenMock(lower_="caca", pos_="dummy")
    assert get_sirrematic_relation_words_verbs_enjambment(previous_token,
                                                          next_token) is None


def test_get_sirrematic_relation_words_verbs_enjambment_aux_de():
    previous_token = TokenMock(pos_="AUX")
    next_token = TokenMock(lower_="de", pos_="dummy", tag_="AdpType=Prep")
    assert get_sirrematic_relation_words_verbs_enjambment(previous_token,
                                                          next_token) == ['AUX',
                                                                          'PREP']


def test_get_sirrematic_relation_words_verbs_enjambment_aux_del():
    previous_token = TokenMock(pos_="AUX")
    next_token = TokenMock(lower_="del", pos_="dummy", tag_="AdpType=Prep")
    assert get_sirrematic_relation_words_verbs_enjambment(previous_token,
                                                          next_token) == ['AUX',
                                                                          'PREP']


def test_get_sirrematic_relation_words_verbs_enjambmentverb_de():
    previous_token = TokenMock(pos_="VERB")
    next_token = TokenMock(lower_="de", pos_="dummy", tag_="AdpType=Prep")
    assert get_sirrematic_relation_words_verbs_enjambment(previous_token,
                                                          next_token) == [
               'VERB', 'PREP']


def test_get_sirrematic_relation_words_verbs_enjambment_verb_del():
    previous_token = TokenMock(pos_="VERB")
    next_token = TokenMock(lower_="del", pos_="dummy", tag_="AdpType=Prep")
    assert get_sirrematic_relation_words_verbs_enjambment(previous_token,
                                                          next_token) == [
               'VERB', 'PREP']


def test_get_sirrematic_prepositional_prep_before_noun_or_adjective_enjambment_root_prep():
    previous_token = TokenMock(dep_="ROOT", pos_="NOUN")
    next_token = TokenMock(lower_="dummy", pos_="dummy", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_before_noun_adjective_enjambment(
        previous_token, next_token) == ['NOUN', 'PREP']


def test_get_sirrematic_prepositional_prep_before_noun_or_adjective_enjambment_nsubj_prep():
    previous_token = TokenMock(dep_="nsubj", pos_="NOUN")
    next_token = TokenMock(lower_="dummy", pos_="dummy", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_before_noun_adjective_enjambment(
        previous_token, next_token) == ['NOUN', 'PREP']


def test_get_sirrematic_prepositional_prep_before_noun_or_adjective_enjambment_0_n_rights():
    previous_token = TokenMock(dep_="nsubj", pos_="NOUN")
    next_token = TokenMock(lower_="dummy", pos_="dummy", tag_="AdpType=Prep",
                           n_rights=0)
    assert get_sirrematic_prepositional_before_noun_adjective_enjambment(
        previous_token, next_token) is None


def test_get_sirrematic_prepositional_without_de_enjambment_noun_prep():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="dummy", pos_="PREP", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_without_de_enjambment(previous_token,
                                                              next_token) == [
               'NOUN', 'PREP']


def test_get_sirrematic_prepositional_without_de_enjambment_adj_prep():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="dummy", pos_="PREP", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_without_de_enjambment(previous_token,
                                                              next_token) == [
               'ADJ', 'PREP']


def test_get_sirrematic_prepositional_enjambment_adj_prep():
    previous_token = TokenMock(pos_="ADJ")
    next_token = TokenMock(lower_="dummy", pos_="PREP", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_enjambment(previous_token,
                                                   next_token) == ['ADJ',
                                                                   'PREP']


def test_get_sirrematic_prepositional_enjambment_adv_prep():
    previous_token = TokenMock(pos_="ADV")
    next_token = TokenMock(lower_="dummy", pos_="PREP", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_enjambment(previous_token,
                                                   next_token) == ['ADV',
                                                                   'PREP']


def test_get_sirrematic_prepositional_enjambment_noun_prep():
    previous_token = TokenMock(pos_="NOUN")
    next_token = TokenMock(lower_="dummy", pos_="PREP", tag_="AdpType=Prep",
                           n_rights=1)
    assert get_sirrematic_prepositional_enjambment(previous_token,
                                                   next_token) == ['NOUN',
                                                                   'PREP']


def test_get_link_enjambment_root_dummy():
    previous_token = TokenMock(dep_="ROOT", pos_="dummy")
    next_token = TokenMock(pos_="dummy", tag_="AdpType=Prep", n_rights=1,
                           head=previous_token)
    assert get_link_enjambment(previous_token, next_token) == ['dummy', 'dummy']


def test_get_link_enjambment_nsubj_dummy():
    previous_token = TokenMock(dep_="ROOT", pos_="dummy")
    next_token = TokenMock(pos_="dummy", tag_="AdpType=Prep", n_rights=1,
                           head=previous_token)
    assert get_link_enjambment(previous_token, next_token) == ['dummy', 'dummy']
