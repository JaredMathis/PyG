class grammar_rule_part:
    def __init__(self, part) -> None:
        if type(part) == str:
            part = [*part]
        self.part = part
    
    def __str__(self) -> str:
        return str(self.part)

    def __eq__(self, __o: object) -> bool:
        if type(__o) == str:
            __o = grammar_rule_part(__o)
        return str(self) == str(__o)
    
    def __hash__(self) -> int:
        return hash(str(self))