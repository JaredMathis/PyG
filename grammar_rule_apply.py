from eq import eq
from grammar_rule import grammar_rule
from grammar_rule_part import grammar_rule_part
from int_natural import int_natural
from log_me import log_me


def grammar_rule_apply(current: list, rule, position):
    if type(current) != grammar_rule_part:
        current = grammar_rule_part(current)
    assert type(rule) == grammar_rule
    assert int_natural(position)

    match = current.part[position:position+len(rule.left.part)]
    assert eq(match, rule.left.part)
    result = current.part[:position] + rule.right.part + current.part[position+len(rule.left.part):]
    return grammar_rule_part(result)

assert eq(
    grammar_rule_apply(
        'bae',
        grammar_rule('a', 'cd'),
        1
    ), 
    'bcde')

assert eq(
    grammar_rule_apply(
        'ab',
        grammar_rule('a', 'cd'),
        0
    ), 
    'cdb')