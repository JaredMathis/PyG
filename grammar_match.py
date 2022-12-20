from eq import eq
from grammar import grammar
from grammar_derive import grammar_derive
from grammar_rule import grammar_rule
from grammar_rule_part import grammar_rule_part


def grammar_match(g, start, examples, counters, depth):
    logging = True

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
            if logging:
                print('counter found: ' + str(d))
            return False

    if len(remaining) > 0:
        if logging:
            print('extra found: ' + str([str(r) for r in remaining]))
        return False

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
    grammar_match(
        grammar([grammar_rule('a','aa')]), 
        'a', 
        ['b'], 
        ['a'], 
        0), 
    False)

assert eq(
    grammar_match(
        grammar([grammar_rule('a','aa')]), 
        'a', 
        ['a', 'aa'], 
        [
            'b', 
            'ba', 'ab', 'ba'], 
        1), 
    True)

assert eq(
    grammar_match(
        grammar([grammar_rule('a','ba')]), 
        'a', 
        ['a', 'ba', 'bba'], 
        [
            'b', 
            'ab', 'bb', 'aa', 
            'bab', 'aab', 'abb', 'aab', 'bbb', 'aaa'], 
        2), 
    True)