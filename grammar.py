from eq import eq
from grammar_rule import grammar_rule
from log_me import log_me


class grammar:
    def __init__(self, rules) -> None:
        if type(rules) == grammar_rule:
            rules = [rules]
        self.rules = rules
    
    def __str__(self) -> str:
        return str([str(r) for r in self.rules])

    def __eq__(self, __o: object) -> bool:
        if type(__o) == grammar_rule:
            __o = grammar(__o)
        return str(self) == str(__o)

assert eq(
    grammar(grammar_rule('a','aa')), 
    """["['a'] > ['a', 'a']"]"""
    )
assert eq(
    (grammar([grammar_rule('a','bc'), grammar_rule('b','bb')])), 
    """["['a'] > ['b', 'c']", "['b'] > ['b', 'b']"]"""
    )