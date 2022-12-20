from eq import eq
from grammar_rule import grammar_rule
from grammar_rule_apply_at import grammar_rule_apply_at
from grammar_rule_part import grammar_rule_part


def grammar_rule_apply(current, rule):
    if type(current) != grammar_rule_part:
        current = grammar_rule_part(current)
    assert type(rule) == grammar_rule

    for position in range(len(current.part)):
        try:
            result = grammar_rule_apply_at(current, rule, position)
            yield result
        except:
            pass

def grammar_rule_apply_list(current, rule):
    return [item for item in grammar_rule_apply(current, rule)]

assert eq(
    grammar_rule_apply_list(
        'aaa',
        grammar_rule('a', 'bb')
    ),
    [grammar_rule_part(x) for x in ['bbaa','abba','aabb']]
)