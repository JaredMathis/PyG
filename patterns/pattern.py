from grammar_rule_part import grammar_rule_part


class pattern:
    def __init__(self, examples, counters) -> None:
        self.examples = [grammar_rule_part(e) for e in examples]
        self.counters = [grammar_rule_part(c) for c in counters]
    
    def __str__(self) -> str:
        return str([str(e) for e in self.examples]) + ":" + str([str(c) for c in self.counters])