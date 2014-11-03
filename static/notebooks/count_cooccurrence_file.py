from count_cooccurrence import count_cooccurrence
from util import corpus


def count_cooccurrence_file(f_name):
    return count_cooccurrence(corpus([f_name]))