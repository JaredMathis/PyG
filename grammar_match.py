from grammar import grammar
from grammar_derive import grammar_derive
from grammar_rule import grammar_rule
from grammar_rule_part import grammar_rule_part


def grammar_match(g, start, examples, counters, depth):
    assert type(g) == grammar
    assert type(examples) == list
    assert type(counters) == list

    examples = [grammar_rule_part(e) for e in examples]
    counters = [grammar_rule_part(c) for c in counters]

    remaining = set(examples)
    set_counters = set(counters)

    for d in grammar_derive(g, start, depth):
        if d in remaining:
            remaining.remove(d)
        if d in set_counters:
            print('counter found: ' + str(d))
            return False

    if len(remaining) > 0:
        print('extra found: ' + str([str(r) for r in remaining]))
        return False

    return True

print(grammar_match(grammar([grammar_rule('a','aa')]), 'a', ['a'], ['b'], 3))