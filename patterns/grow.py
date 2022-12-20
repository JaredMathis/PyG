from patterns.pattern import pattern


def pattern_grow():
    return pattern(
        [
            'a', 
            'aa'
        ], 
        [
            'b', 
            'ba', 
            'ab', 
            'ba'
        ])