from grammar import grammar
from grammar_cf_random import grammar_cf_random
from grammar_match import grammar_match
from grammar_rule import grammar_rule
from int_natural import int_natural
from patterns.grow import pattern_grow


def grammars_cf_search(symbols, pattern):
    symbols, start = symbols_parse(symbols)

    i = 1
    while True:
        g = grammar_cf_random(symbols, i)
        result = grammar_match(g, start, pattern.examples, pattern.counters, 3)
        if result == True:
            return g

def symbols_parse(symbols):
    if (int_natural(symbols)):
        symbols = range(symbols)
    assert len(symbols) >= 1
    symbols = [str(s) for s in symbols]

    start = symbols[0]
    return symbols,start

def test(pattern):
    g = grammars_cf_search(2, pattern)
    return type(g) == grammar

patterns = [
    pattern_grow()
]
for p in patterns:
    assert test(p)


