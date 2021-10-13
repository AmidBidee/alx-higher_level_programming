"""
write_file: Writes a text to file.
"""


def write_file(filename="", text=""):
    """ writes text to file returns length of text """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
