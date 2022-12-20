from grammar import grammar
from grammar_derive import grammar_derive


def grammar_match(g, start, examples, counters, depth):
    assert type(g) == grammar
    assert type(examples) == list
    assert type(counters) == list

    remaining = set(examples)
    set_counters = set(counters)

    for d in grammar_derive(g, start, depth):
        if remaining[d]:
            remaining.remove(d)
        if set_counters[d]:
            return False

    if len(remaining) > 0:
        return False

    return True

print()