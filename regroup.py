import random
from itertools import chain, cycle


def regroup(n, groups):
    """Return n new groups built from given groups."""
    result = tuple([] for _ in range(n))
    for item, new_group in zip(chain(*groups), cycle(result)):
        new_group.append(item)
    return result


def shuffle(groups):
    """Return new list of groups, shuffled but not mixed."""
    groups = [list(group) for group in groups]  # copy args
    for group in groups:
        random.shuffle(group)  # shuffle items in each group
    random.shuffle.groups()  # shuffle groups
    return groups
