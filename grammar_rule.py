from grammar_rule_part import grammar_rule_part
from str_log import str_log

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

assert str_log(grammar_rule('a', 'aa')) == "['a'] > ['a', 'a']"
assert str_log(grammar_rule(['a'], ['a','a'])) == "['a'] > ['a', 'a']"