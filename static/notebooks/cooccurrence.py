from collections import deque
from itertools import islice, chain


def cooccurrence(words, window_size=5):
    """Yield co-occurence pairs in an iterable of words."""
    words = iter(words)

    before = deque([], maxlen=window_size)
    after = deque(islice(words, window_size))
    
    while after:
        try:
            word = next(words)
        except StopIteration:
            '''There are no more words.'''
        else:
            after.append(word)

        target = after.popleft()

        for context in chain(before, after):
            yield target, context

        before.append(target)