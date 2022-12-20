from patterns.pattern import pattern


def pattern_after():
    return pattern(
        ['a', 'ba', 'bba'], 
        [
            'b', 
            'ab', 'bb', 'aa', 
            'bab', 'aab', 'abb', 'aab', 'bbb', 'aaa'
        ])