from eq import eq
from grammar import grammar
from grammar_derive import grammar_derive
from grammar_rule import grammar_rule
from grammar_rule_part import grammar_rule_part
from patterns.after import pattern_after
from patterns.grow import pattern_grow


def grammar_match(g, start, examples, counters, depth):
    assert type(g) == grammar
    assert type(examples) == list
    assert type(counters) == list

    examples = [grammar_rule_part(e) for e in examples]
    counters = [grammar_rule_part(c) for c in counters]

    remaining = set(examples)
    set_counters = set(counters)

    if len(remaining.intersection(set_counters)) > 0:
        raise "Examples and Counters must be mutually exclusive"

    for d in grammar_derive(g, start, depth):
        if d in remaining:
            remaining.remove(d)
        if d in set_counters:
            return 'counter found: ' + str(d)

    if len(remaining) > 0:
        return 'extra found: ' + str([str(r) for r in remaining])

    return True

assert eq(
    grammar_match(
        grammar([grammar_rule('a','aa')]), 
        'a', 
        ['a'], 
        ['b'], 
        0), 
    True)

assert eq(
    type(
        grammar_match(
            grammar([grammar_rule('a','aa')]), 
            'a', 
            ['b'], 
            ['a'], 
            0)
    ), 
    str)

assert eq(
    grammar_match(
        grammar([grammar_rule('a','aa')]), 
        'a', 
        pattern_grow().examples, 
        pattern_grow().counters, 
        1), 
    True)

assert eq(
    grammar_match(
        grammar([grammar_rule('a','ba')]), 
        'a', 
        pattern_after().examples, 
        pattern_after().counters,  
        2), 
    True)