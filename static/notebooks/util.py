from itertools import chain


def read_words(f_name):
    """Read a file word by word."""
    with open(f_name) as f:
        for line in f:
            line.strip()
            
            # Tokenization is a difficult task,
            # a word is anythin between two spaces.
            for word in line.split():
                yield word


def clean_words(words):
    """Clean up words."""
    for word in words:
        w = ''.join(ch for ch in word.lower() if ch.isalpha())

        if w:
            yield w

        
def corpus(f_names):
    """Treat a collection of files as a single resource."""
    return chain.from_iterable(clean_words(read_words(f)) for f in f_names)
    