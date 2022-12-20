from patterns.pattern import pattern


def pattern_grow():
    return pattern(
        [
            '0', 
            '00'
        ], 
        [
            '1', 
            '10', 
            '01', 
            '10'
        ])