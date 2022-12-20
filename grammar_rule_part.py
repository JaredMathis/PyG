class grammar_rule_part:
    def __init__(self, part) -> None:
        if type(part) == grammar_rule_part:
            part = part.part
        if type(part) != list:
            assert type(part) == str
            part = [*part]
        for p in part:
            assert type(p) == str
        self.part = part
    
    def __str__(self) -> str:
        return str(self.part)

    def __eq__(self, __o: object) -> bool:
        if type(__o) == str:
            __o = grammar_rule_part(__o)
        return str(self) == str(__o)
    
    def __hash__(self) -> int:
        return hash(str(self))