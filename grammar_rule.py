from grammar_rule_part import grammar_rule_part

class grammar_rule:
    def __init__(
        self, 
        left: grammar_rule_part, 
        right: grammar_rule_part) -> None:
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return self.left + ' > ' + self.right

g = grammar_rule('a', 'aa')

print(g)