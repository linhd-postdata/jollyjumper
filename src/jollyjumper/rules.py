def get_sirrematic_enjambment(previous_token, next_token):
    """
    Checks if sirrematic enjambment exists between two lines
    :param previous_token: The word before a newline character
    :param next_token: The word after a newline character
    :return: Sirrematic pair or None if not found
    """
    sirremactic_pairs = [['ADJ', 'NOUN'],
                         ['ADV', 'NOUN'],
                         ['ADP', 'ADJ'],
                         ['ADP', 'NOUN'],
                         ['ADJ', 'ADV'],
                         ['ADV', 'VERB']
                         ]
    while sirremactic_pairs:
        sirrematic_pair = sirremactic_pairs.pop()
        if sorted((previous_token.pos_, next_token.pos_)) == sorted(sirrematic_pair)\
                and (next_token.is_ancestor(previous_token) or previous_token.is_ancestor(next_token)):
            return sirrematic_pair
    return None


rules = locals()