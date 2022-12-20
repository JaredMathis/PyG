from grammar_rule import grammar_rule
from int_natural import int_natural


def grammars_cf_search(symbols):
    if (int_natural(symbols)):
        symbols = range(symbols)
    assert len(symbols) >= 1

    start = symbols[0]
    rules = []

    # rules.append(grammar_rule(start, ))



