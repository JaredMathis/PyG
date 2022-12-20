from patterns.pattern import pattern


def pattern_after():
    return pattern(
        ['0', '10', '110'], 
        [
            '1', 
            '01', '11', '00', 
            '101', '001', '011', '001', '111', '000'
        ])