#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    Converts a Roman numeral to a Hindu-Arabic numeral integer
    Parameters:
    roman_string (str): The string consisting of roman numeral symbols
    Returns:
    An integer representation of the Roman numeral
    '''
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0
    sym_tbl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_symbols = set(sym_tbl.keys())
    res = 0
    str_len = len(roman_string)
    prev_symbol = 'I'
    for char in reversed(roman_string):
        c = ord(char)
        is_lower = (c >= ord('a')) and (c <= ord('z'))
        offset = (1 << 5) if is_lower else 0
        sym = chr(c - offset)
        if sym not in roman_symbols:
            return 0
        if sym_tbl[sym] < sym_tbl[prev_symbol]:
            res -= sym_tbl[sym]
        else:
            res += sym_tbl[sym]
        prev_symbol = sym
    return res
