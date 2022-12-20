from eq import eq
from grammar import grammar
from grammar_rule import grammar_rule
from grammar_rule_apply import grammar_rule_apply
from grammar_rule_part import grammar_rule_part
from int_natural import int_natural
from log_me import log_me


def grammar_derive(g, start, depth):
    assert type(g) == grammar
    if type(start) != grammar_rule_part:
        start = grammar_rule_part(start)
    yield start
    if (depth <= 0):
        return
    assert int_natural(depth)

    for rule in g.rules:
        for applied in grammar_rule_apply(start, rule):
            for child in grammar_derive(g, applied, depth - 1):
                yield child

def grammar_derive_list(g, start, depth):
    return [d for d in grammar_derive(g, start, depth)]

def grammar_derive_list_str(g, start, depth):
    return str([str(d) for d in grammar_derive_list(g, start, depth)])

assert eq(
    (grammar_derive_list_str(grammar(grammar_rule('a', 'aa')), 'a', 2)),
    """["['a']", "['a', 'a']", "['a', 'a', 'a']", "['a', 'a', 'a']"]"""
    )