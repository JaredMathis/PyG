from eq import eq
from grammar_rule_part import grammar_rule_part
from log_result import log_result

class grammar_rule:
    def __init__(
        self, 
        left, 
        right) -> None:

        if (type(left) != grammar_rule_part):
            left = grammar_rule_part(left)
        if (type(right) != grammar_rule_part):
            right = grammar_rule_part(right)

        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return str(self.left) + ' > ' + str(self.right)

assert eq(
    str(grammar_rule('a', 'aa')), 
    "['a'] > ['a', 'a']")
assert eq(
    str(grammar_rule('a', 'aa')), 
    "['a'] > ['a', 'a']")
assert eq(
    str(grammar_rule(['a'], ['a','a'])), 
    "['a'] > ['a', 'a']")