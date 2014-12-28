# -*- coding: utf-8 -*-

"""Utilities for collections"""


def pretty_dict(dic):
    """Printable string representation of a dictionary
       - items are listed in alphabetical order of their keys,
         to ensure a deterministic representation
         (e.g. for unit tests)
    """
    items = []
    keys = sorted(dic.keys())
    for key in keys:
        val = dic[key]
        if isinstance(val, dict):
            val = pretty_dict(val)
        item_str = '{}: {}'.format(key, val)
        items.append(item_str)
    return '{' + ', '.join(items) + '}'
