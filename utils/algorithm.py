from itertools import groupby


def rle(string):
    """Run Length Encoding"""
    rle_list = []
    for k, group in groupby(string):
        rle_list.append((k, len(tuple(group))))
    return rle_list
