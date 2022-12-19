from grammar_rule_part import grammar_rule_part

class grammar_rule:
    def __init__(
        self, 
        left, 
        right) -> None:

        assert 1 == 1

        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return str(self.left) + ' > ' + str(self.right)

g = grammar_rule(
    grammar_rule_part('a'), 
    grammar_rule_part('aa'))

print(g)