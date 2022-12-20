import random
from grammar import grammar
from grammar_rule import grammar_rule
from grammar_rule_part import grammar_rule_part
from int_natural import int_natural


def grammar_random(symbols, rule_count=None):
    if int_natural(symbols):
        symbols = range(symbols)
    if rule_count == None:
        rule_count = len(symbols)

    rules = []
    
    for i in symbols:
        rules.append(grammar_rule_random(symbols))

    return grammar(rules)

def grammar_rule_random(symbols):
    small = [random.choice(symbols)]
    big = [random.choice(symbols), random.choice(symbols)]
    return grammar_rule(small, big)

print(grammar_random(3))