import pandas as pd

from cooccurrence import cooccurrence


def count_cooccurrence(words):
    """Count co-occrence counts.
    
    :param iter words: an iterable of words.
    
    :return: a pandas.DataFrame where `target` and`context`
             are the index columns and `count` is a data column.
    
    """
    frame = pd.DataFrame(
        cooccurrence(words),
        columns=('target', 'context'),
    )
    
    frame['count'] = 1
    
    return frame.groupby(('target', 'context')).sum()