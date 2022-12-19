class grammar_rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return self.left + ' > ' + self.right

g = grammar_rule('a', 'aa')

print(g)