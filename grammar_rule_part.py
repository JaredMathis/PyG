class grammar_rule_part:
    def __init__(self, part) -> None:
        if type(part) == type(str):
            part = part.split()
        self.part = part
    
    def __str__(self) -> str:
        return str(self.part)